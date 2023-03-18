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
    return "(" + prompt + ":" + str(weight) + "), "

#pass in string OR prompt element(list)
def create_prompt(prompt, base_weight : float = cfg.base_weight, norand_weights : bool = False) -> str:
    
    weight = 1.0
    prompt_str = ""

    #if prompt is a string
    if(isinstance(prompt, str)):
        #use a random weight
        prompt_str = prompt
    

    
    #if prompt is a prompt element
    if(isinstance(prompt, list)):
        prompt_str = prompt[0]
        #if norand modifier
        if(len(prompt) == 3 or norand_weights):
            norand_weights = True
            base_weight = prompt[1]
    
    #assert(len(prompt_str) != 0)
    if(not norand_weights):
        weight = rand_weight(base_weight)
    else:
        weight = base_weight
    return create_weighted_tag(prompt_str, weight)





def parse_LORA(lora_e : cfgutils.LORA) -> str:
    #check for overrides
    if(lora_e.weight != None):
            base_weight = lora_e.weight
        
    if(lora_e.norand != True):
        weight = rand_weight(base_weight)
    else:
        weight = base_weight
    #generate lora prompt first
    out = lora_e.lora_tostr(weight)
    out += ", "
    for v in lora_e.bundled_tags:
        out += create_prompt(v, base_weight, lora_e.norand)

        #out += create_prompt(v, base_weight, prompt.norand)
    return out

def parse_RandTable(tab_e : cfgutils.RandTable) -> str:
        #if randtable
        out : str = ""
        elements = tab_e.get_rand_elements()
        for v in elements:
            if(isinstance(v, str)):
                elist : list = [v, tab_e.base_weight]
                if(tab_e.norand):
                    elist.append(cfgutils.NORAND)
                out += parse_element(elist)
                continue

            out += parse_element(v)
        return out



#parses ANY element in the prompt list and returns string version
def parse_element(element) -> str:
    #honestly i could customize weight randrange for randtables too but lazy
    
    if(isinstance(element, cfgutils.RandTable)):
        return parse_RandTable(element)
    
    if(isinstance(element, cfgutils.RandElement)):
        if(element.trigger()):
            return parse_element(element.element)
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
    return create_prompt(element)

    

def gen_seed() -> int:
    #2^63 - 1
    return random.randint(0,9223372036854775808)

def mkdir_if_not_exist(dir : str):
    if(not os.path.isdir(dir)):
        os.mkdir(dir)
    
def mk_subdirs(root : str):
    for i in range(0, cfg.split_to):
        mkdir_if_not_exist(root + str(i))
        