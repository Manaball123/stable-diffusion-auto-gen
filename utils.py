import cfg
import numpy as np
import random
import cfgutils
import os

def rand_weight(base : float = cfg.base_weight) -> float:
    if(cfg.normally_distributed):
        return np.random.normal(base, cfg.max_tag_weight_offset)
    return (random.random() - 0.5) * 2
    


def create_weighted_tag(prompt : str, weight : float) -> str:
    #dont make it weighted if deviates too small from 1
    if(weight < 0.99 or weight > 1.01):
        return "(" + prompt + ":" + str(weight) + "), "
    return prompt + ", "

#disregards any default params
def create_prompt_raw(prompt : str, weight : float, norand : bool) -> str:
    if(not norand):
        weight = rand_weight(weight)
    return create_weighted_tag(prompt, weight)

def get_override_traits(element : list) -> cfgutils.ElementTraits:
    traits : cfgutils.ElementTraits = cfgutils.ElementTraits(cfg.base_weight, cfg.randomize_tag_weight)
    if(isinstance(element, list)):
        #if norand modifier
        if(len(element) == 3):
            traits.norand = True
        traits.base_weight = element[1]
    
    #use default args if not list
    return traits



#pass in string OR prompt element(list)
def create_prompt(prompt, traits : cfgutils.ElementTraits = None) -> str:
    
    traits = get_override_traits(prompt)
    p_str = prompt
    if(isinstance(prompt, list)):
        p_str = prompt[0]

    return create_prompt_raw(p_str, traits.base_weight, traits.norand)


def parse_LORA(lora_e : cfgutils.LORA) -> str:
    #check for overrides
    base_weight = lora_e.traits.base_weight
    
    if(lora_e.traits.norand):
        weight = base_weight
    else:
        weight = rand_weight(base_weight)
    #generate lora prompt first
    out = lora_e.lora_tostr(weight)
    out += ", "
    for v in lora_e.bundled_tags:
        out += parse_element(v, )


    return out

def parse_RandTable(tab_e : cfgutils.RandTable) -> str:
        #if randtable
        out : str = ""
        elements = tab_e.get_rand_elements()
        for v in elements:

            out += parse_element(v, tab_e.traits)
        return out



#parses ANY element in the prompt list and returns string version
def parse_element(element, traits : cfgutils.ElementTraits = None) -> str:
    #honestly i could customize weight randrange for randtables too but lazy
    
    if(isinstance(element, cfgutils.RandTable)):
        #no trait inheritance
        return parse_RandTable(element)
    
    if(isinstance(element, cfgutils.RandElement)):
        if(element.trigger()):
            return parse_element(element.element, traits)
        return ""
    
    #if bundle
    if(isinstance(element, cfgutils.ElementBundle)):
        out : str = ""
        #for VALUE in CONTENTS of BUNDLE
        for v in element.elements:
            out += parse_element(v)
        return out
    
    #if unmodified list
    if(isinstance(element, cfgutils.UnmodifiedList)):
        return element.get_str()
    #if its a LORA
    if(isinstance(element, cfgutils.LORA)):
        return parse_LORA(element)

    #else parse as normal
    return create_prompt(element, traits)

    

def gen_seed() -> int:
    #2^63 - 1
    return random.randint(0,9223372036854775808)

#creates the dir only if the directory doesnt exist yet
#os.mkdir doesn't work if the dir already does
def mkdir_if_not_exist(dir : str):
    if(not os.path.isdir(dir)):
        os.mkdir(dir)
    
def mk_subdirs(root : str):
    for i in range(0, cfg.split_to):
        mkdir_if_not_exist(root + str(i))
        