import requests
import base64
import os
import time
import cfg
import numpy as np
import utils
import json
gen_payload = {
    "prompt" : "",
    "negative_prompt" : cfg.negative_prompt,
    "steps" : cfg.steps,
    "width" : cfg.width,
    "height" : cfg.height,
    "batch_size" : cfg.batch_size,
    "cfg_scale" : cfg.cfg_scale,
    "sampler_name" : cfg.sampler_name,
    "seed" : -1
}

upscale_payload = {
  "resize_mode": 0,
  "show_extras_results": True,
  "gfpgan_visibility": 0,
  "codeformer_visibility": 0,
  "codeformer_weight": 0,
  "upscaling_resize": cfg.upscaling_resize,
#  "upscaling_resize_w": 512,
#  "upscaling_resize_h": 512,
  "upscaling_crop": True,
  "upscaler_1": cfg.upscaler_1,
  "upscaler_2": cfg.upscaler_2,
  "extras_upscaler_2_visibility": 0,
  "upscale_first": False,
  "image": ""
}

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

def save_image(data : bytes, id : int, app_str : str = ""):
    
    fname : str = get_fname(id, cfg.img_dir, ".png", app_str)
    log("Saving " + fname)
    with open(fname, "wb+") as f:
        f.write(data)
    

def save_metadata(id : int):
    data = {
        "gen_payload" : gen_payload
    }
    if(cfg.upscale_image):
        data["upscale_payload"] = upscale_payload
    fname : str = get_fname(id, cfg.metadata_dir, ".json")
    with open(fname, "w") as f:
        f.write(json.dumps(data, indent=1))

    

def mkdir():
    utils.mkdir_if_not_exist(cfg.root_dir)
    utils.mkdir_if_not_exist(cfg.img_dir)
    utils.mkdir_if_not_exist(cfg.metadata_dir)
    if(not cfg.split_dirs):
        return
    
    for i in range(0, cfg.split_to):
        idir = cfg.img_dir + str(i)
        mdir = cfg.metadata_dir + str(i)
        utils.mkdir_if_not_exist(idir)
        utils.mkdir_if_not_exist(mdir)

        
    


def main():
    stop_generation : bool = False
    mkdir()
    ctr : int = 0
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
            save_image(image, id, "-original")
            if(cfg.upscale_image):
                upscale_payload["image"] = v
                upscale_resp = requests.post(url = f"{cfg.url}/sdapi/v1/extra-single-image", json = upscale_payload)
                if(upscale_resp.status_code != 200):
                    log("Upscaling request failed. Proceeding without upscaling...")
                else:
                    upscale_obj = upscale_resp.json()
                    v_upscaled = upscale_obj["image"]
                    image_upscaled = base64.b64decode(v_upscaled)
                    save_image(image_upscaled, id, "-upscaled")
                #clear upscale image payload
                upscale_payload['image'] = "(omitted)"
            save_metadata(id)
        if(cfg.no_gen_limit == False):
            ctr += 1
            if(ctr >= cfg.images_n):
                log("Generated sufficient images. Terminating...")
                return
              
        
    return



if __name__ == "__main__":
    main()