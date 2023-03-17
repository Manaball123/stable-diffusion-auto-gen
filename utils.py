import cfg
import numpy as np
import random

def rand_weight(base : float = cfg.base_weight) -> float:
    if(cfg.normally_distributed):
        return np.random.normal(base, cfg.max_tag_weight_offset)
    return (random.random() - 0.5) * 2
    


def create_weighted_tag(prompt : str, weight : float) -> str:
    return "(" + prompt + ":" + str(weight) + "), "

#pass in string OR prompt element(list)
def create_prompt(prompt, base_weight : float = cfg.base_weight, norand_weights : bool = False) -> str:
    
    
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
    
    assert(len(prompt_str) != 0)
    if(not norand_weights):
        base_weight = rand_weight(base_weight)
    return create_weighted_tag(prompt_str, base_weight)




#parses ANY element in the prompt list and returns string version
def parse_element(element) -> str:
    #honestly i could customize weight randrange for randtables too but lazy
    
    if(isinstance(element, cfg.RandTable)):
        #if randtable
        out : str = ""
        elements = element.get_rand_elements()
        for v in elements:
            out += create_prompt(v, element.base_weight, element.norand)
        return out
    #else parse as normal
    return create_prompt(element)

    
    