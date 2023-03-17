import random
#ignore this thing ig
#randomize prompts in this table
class RandTable:
    def __init__(self, elements : list, elements_n : int, def_weight : float = 1.0, lock_weights : bool = False) -> None:
        """
        elements: prompts in table
        elements_n: number of prompts to use
        def_weight: base prompt weight for every prompt, note that overrides will still work
        
        """
        self.elements = elements
        self.elements_n = elements_n
        self.base_weight = def_weight
        self.norand = lock_weights
        
        return
    def get_rand_elements(self) -> list:
        return random.sample(self.elements, self.elements_n)

#ensured that the contents are appended as is
class UnmodifiedList:
    def __init__(self, elements : list) -> None:
        self.elements = elements
    #returns string representation of the object
    def get_str(self)->str:
        out : str = ""
        for v in self.elements:
            out += v
            out += ","
        return out

#Note that you can put this inside a rand table
class LORA:
    #note that bundled tags inherit these
    def __init__(self, name : str, weight : float = None, norand : bool = True, bundled_tags : list = []):
        self.name = name
        self.weight = weight
        self.norand = norand
        self.bundled_tags = bundled_tags
    #converts LORA to string
    #note that this does not affect the other stuff
    def lora_tostr(self, weight : float) -> str:
        if(weight == None):
            weight = 1.0
        return "<lora:" + self.name + ":" + str(weight) + ">"

#element that has a random chance to appear
class RandElement:
    def __init__(self, element, probability : float = 0.5):
        self.element = element
        self.probability = probability
    def trigger(self) -> bool:
        if(random.random() < self.probability):
            return True
        return False

#most of these are just for type checking tbh
class ElementBundle:
    def __init__(self, elements : list):
        self.elements = elements


    
    

        
    
NORAND = True
