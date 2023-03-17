import requests
import base64
import os
import time
import cfg
import numpy as np
import utils

gen_payload = {
    "prompt" : "",
    "negative_prompt" : cfg.negative_prompt,
    "steps" : cfg.steps,
    "width" : cfg.width,
    "height" : cfg.height,
    "batch-size" : cfg.batch_size,
    "cfg_scale" : cfg.cfg_scale
}

upscale_payload = {

}

#simple wrapper
def log(v):
    if(cfg.print_logs):
        print(v)

def get_fname():
    id = time.time_ns() // 100
    if(cfg.split_dirs):
        subdir = cfg.root_dir + str(id % 100) + "/"
    else:
        subdir = cfg.root_dir
    return subdir + str(id) + ".png"

def save_image(data : bytes):
    fname : str = get_fname()
    log("Saving " + fname)
    with open(fname, "wb+") as f:
        f.write(data)
    


def mkdir():
    if(not os.path.isdir(cfg.root_dir)):
        os.mkdir(cfg.root_dir)
    if(not cfg.split_dirs):
        return
    
    for i in range(0, cfg.split_to):
        cdir = cfg.root_dir + str(i)
        if(not os.path.isdir(cdir)):
            os.mkdir(cdir)

def main():
    stop_generation : bool = False
    mkdir()
    ctr : int = 0
    while(not stop_generation):
        prompts : str = ""
        for v in cfg.prompt_list:
            prompts += utils.parse_element(v)

        gen_payload["prompt"] = prompts
        log("Generating with prompts: " + prompts)
        #thx 2 the webui github docs thingy
        resp = requests.post(url=f'{cfg.url}/sdapi/v1/txt2img', json = gen_payload)
        if(resp.status_code != 200):
            log("Request failed. Retrying...")
            continue
        
        log("Generation success. Saving images...")
        resp_obj = resp.json()
        
        for v in resp_obj["images"]:
            if(cfg.upscale_image):
                pass
            
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