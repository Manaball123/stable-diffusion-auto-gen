import requests
import base64
import os
import time
import cfg
import numpy as np
import utils
import json

#I know this is saved in the image data and stuff, but I'm still saving this because u can get the same image by sending the same json
gen_payload = {
    "prompt" : "",
    "negative_prompt" : cfg.negative_prompt,
    "steps" : cfg.steps,
    "width" : cfg.width,
    "height" : cfg.height,
    "batch_size" : cfg.batch_size,
    "cfg_scale" : cfg.cfg_scale,
    "sampler_name" : cfg.sampler_name,
    "enable_hr" : cfg.enable_hr,
    "hr_scale" : cfg.hr_scale,
    "hr_upscaler" : cfg.hr_upscaler,
    "denoising_strength" : cfg.hr_denoise_strength,
    "hr_second_pass_steps" : cfg.hr_steps,
    "seed" : -1
}

current_pnginfo = ""



#simple wrapper
def log(v):
    if(cfg.print_logs):
        print(v)

def get_fname(id : int, dir : str, ext : str, app_str : str = ""):
    
    if(cfg.split_dirs):
        subdir = dir + str(id % 100) + "/"
    else:
        subdir = dir
    return subdir + str(id) + app_str + ext

def save_image(data : bytes, id : int):
    
    fname : str = get_fname(id, cfg.img_dir, ".png")
    log("Saving " + fname)
    with open(fname, "wb+") as f:
        f.write(data)
    

def save_metadata(id : int):
    data = {
        "gen_payload" : gen_payload,
        "png_info" : current_pnginfo
    }
    fname : str = get_fname(id, cfg.metadata_dir, ".json")
    with open(fname, "w") as f:
        f.write(json.dumps(data, indent=1))

    

def mkdir():
    utils.mkdir_if_not_exist(cfg.root_dir)
    utils.mkdir_if_not_exist(cfg.img_dir)

    utils.mkdir_if_not_exist(cfg.metadata_dir)
    if(not cfg.split_dirs):
        return
    
    utils.mk_subdirs(cfg.metadata_dir)
    utils.mk_subdirs(cfg.img_dir)
    
        
    


def main():
    global current_pnginfo
    stop_generation : bool = False
    mkdir()
    ctr : int = 0
    #interrupt whatever it is that its currently doing
    requests.post(url=f'{cfg.url}/sdapi/v1/interrupt')
    #u can actually send an interrupt request here
    while(not stop_generation):
        prompts : str = ""
        for v in cfg.prompt_list:
            prompts += utils.parse_element(v)

        gen_payload["prompt"] = prompts
        gen_payload["seed"] = utils.gen_seed()

        log("Generating with prompts: " + prompts)
        #thx 2 the webui github docs thingy
        resp = requests.post(url=f'{cfg.url}/sdapi/v1/txt2img', json = gen_payload)
        if(resp.status_code != 200):
            log("Request failed. Retrying...")
            continue
        
        log("Generation success. Saving images...")
        resp_obj = resp.json()
        
        for v in resp_obj["images"]:
        
            image = base64.b64decode(v)
            id = time.time_ns() // 100
            save_image(image, id)

            pnginfo_resp = requests.post(url = f'{cfg.url}/sdapi/v1/png-info', json={"image" : v})
            if(pnginfo_resp.status_code != 200):
                log("PNGInfo request failed.")
                current_pnginfo = ""
            else:
                current_pnginfo = pnginfo_resp.json()["info"]
            save_metadata(id)
            
        if(cfg.no_gen_limit == False):
            ctr += 1
            if(ctr >= cfg.images_n):
                log("Generated sufficient images. Terminating...")
                return
              
        
    return



if __name__ == "__main__":
    main()