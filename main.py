import requests
import base64
import os
import time
import cfg
import random


payload = {
    "prompt" : cfg.prompt,
    "negative_prompt" : cfg.negative_prompt,
    "steps" : cfg.steps,
    "width" : cfg.width,
    "height" : cfg.height,
    "batch-size" : cfg.batch_size,
    "cfg_scale" : cfg.cfg_scale
}

#simple wrapper
def log(v):
    if(cfg.print_logs):
        print(v)

def get_fname():
    return str(time.time_ns())

def save_image(data : bytes):
    fname : str = cfg.root_dir + get_fname() + ".png"
    log("Saving " + fname)
    with open(fname, "wb+") as f:
        f.write(data)
    
def concat_prompts(selection : list):
    out : str = ""
    
    for v in selection:
        out += ", "
        out += v
    
    return out
        
    

def mkdir():
    if(not os.path.isdir(cfg.root_dir)):
        os.mkdir(cfg.root_dir)

def main():
    stop_generation : bool = False
    mkdir()
    ctr : int = 0
    while(not stop_generation):
        #thx 2 the webui github docs thingy
        if(cfg.add_random_prompts):
            prompt_str = concat_prompts(random.sample(cfg.random_prompts, cfg.random_n))
            payload["prompt"] = cfg.prompt + prompt_str

        resp = requests.post(url=f'{cfg.url}/sdapi/v1/txt2img', json = payload)
        if(resp.status_code != 200):
            log("Request failed. Retrying...")
            continue
        
        log("Generation success. Saving images...")
        resp_obj = resp.json()
        
        for v in resp_obj["images"]:
            image = base64.b64decode(v)
            save_image(image)
        if(cfg.no_gen_limit == False):
            ctr += 1
            if(ctr >= cfg.images_n):
                log("Generated sufficient images. Terminating...")
                return
                    
            
        
    return 
if __name__ == "__main__":
    main()