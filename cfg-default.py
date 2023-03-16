
#other shit
url : str = "http://127.0.0.1:7860"
root_dir : str = "./generated-images/"

#self explanatory
images_n = 100
#turn this on if you want to keep generating
no_gen_limit = True

#i would do split dirs if i feel like it
split_dirs = False

#self explanatory
print_logs = True


#generation configs
steps : int = 20
prompt : str = ""
negative_prompt : str = ""

#larger ones sometimes look hideous even when u add those negative stuff
width = 512
height = 512
#u prob should set this to 1, dont think it matters that much tbh
#ok nvm after some rough testing, higher batch does speed it up
#just dont make it exceed ur vram size
batch_size = 1

