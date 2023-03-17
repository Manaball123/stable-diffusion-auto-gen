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
def create_prompt(prompt, base_weight : float = cfg.base_weight) -> str:
    
    #if prompt is a string

    if(isinstance(prompt, str)):
        #use a random weight
        return create_weighted_tag(prompt, rand_weight(base_weight))
    #if prompt is a prompt element
    if(isinstance(prompt, list)):
        #if no norand modifier 
        if(len(prompt) == 2):
            return create_weighted_tag(prompt[0], rand_weight(prompt[1]))
        #assuming its one with norand
        else:
            return create_weighted_tag(prompt, prompt[1])
    
    raise("what the fuck did u pass in here")

        


#parses ANY element in the prompt list and returns string version
def parse_element(element):
    if()
    
    