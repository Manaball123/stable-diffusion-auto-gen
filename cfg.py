from cfgutils import *
#other shit
url : str = "http://127.0.0.1:7860"
root_dir : str = "./generated-data/"
img_dir : str = root_dir + "images/"
metadata_dir : str = root_dir + "metadata/"

#self explanatory
images_n = 100
#turn this on if you want to keep generating
no_gen_limit = True


#ok so its indexed in image%100
split_dirs = False
split_to : int = 100

#self explanatory
print_logs = True


cfg_scale = 10
#generation configs
steps : int = 32
positive_prompts : list = [
    "huge filesize" , 
    "ultra-detailed", 
    "highres", 
    "extremely detailed", 
    "(best quality:1.2)", 
    "(masterpiece:1.3)"
]

sampler_name = "DPM++ 2M Karras"

#to override bias add element in format
#["tag", bias : int]
#to lock weight:
#["tag", bias : int, NORAND]
#sort of like a macro


#picks some random ones to add 
#i cant actually think of any so im just sticking with hair color rn lol
randomize_tag_weight : bool = True
#base weight, can be overridden
base_weight : float = 1.0
#this is treated as the standard deviation if weight is normally distrubuted
max_tag_weight_offset : float = 0.1
normally_distributed : bool = True
add_random_prompts : bool = True

#larger ones sometimes look hideous even when u add those +-
# ngative stuff


width = 1024; height = 768
#width = 2048; height = 1536
#width = 512; height = 512
#width = 768; height = 512
#width = 640; height = 1024
#width = 1024; height = 1024
#u prob should set this to 1, dont think it matters that much tbh
#ok nvm after some rough testing, higher batch does speed it up
#just dont make it exceed ur vram size
#actually this thing doesnt actually matter i think
batch_size = 1

#you get NO postprocessed upscaling, fuck you
upscale_image = True
upscale_w = 1024; upscale_h = 1024
upscaling_resize = 4
upscaler_1 = "R-ESRGAN 4x+"
upscaler_2 = "None"


#list of prompts for generation
prompt_list : list = [
    UnmodifiedList(positive_prompts),
    ["nsfw", 1.2, NORAND],
    "sweat",
    "feet",
    "toes",
    RandElement(ElementBundle([
    "cum on body",
    "cum in pussy",
    "cum pool",
    ]), 0.7),
    
    "breast out",
    RandTable([
    "multiple girls",
    "1girl"
    ], 1, 1.2, True),
    "pussy",
    "nipples",
    "puffed nipples",
    ["small breasts", 1.3, NORAND],
    "skinny",
    "heavy breathing",
    "cute",
    ["sex", 1.2],
    RandElement("looking at viewer", 0.6),
    "blush",
    "long hair",
    RandElement("open mouth", 0.6),
    "breasts",
    RandTable([
    "red hair",
    "blue hair",
    "black hair",
    "blond hair",
    "white hair",
    ["rainbow hair", 1.3],
    ], 1, 1.2, True),
    #RandElement(LORA("ahegao_v1", 1.2, True, ["ahegao", "rolling eyes", "tongue out", "saliva", "drooling"]), 0.1),
    #LORA("lucyCyberpunk_35Epochs", 0.8, True, ["lucy \(cyberpunk\), 1girl, arm up, asymmetrical hair, belt, bodysuit, covered mouth, covered navel, detached sleeves, grey eyes, hip vent, holding, holding weapon, looking at viewer, night, night sky, pouch, short hair, sky, solo, weapon, white hair, wire, short shorts, shorts, open jacket,", ["robot joints", 0.5, NORAND]]),
    RandTable([
    "on side",
    "spread legs",
    "lying",
    LORA("povSquattingCowgirlLora_pscowgirl", 1, bundled_tags = [["squatting cowgirl, cowgirl", 1.2, NORAND]]),
    LORA("grabbingOwnAss_v1", 1.3, bundled_tags = ["grabbing own ass", "ass spread", "ass stretch"])
    ], 1, 1.2, True),
    #["stockings", 1.5]
]

#hahahhaha
#negative_prompt : str = "((poorly drawn hands)),more than 1 left hand, more than 1 right hand, short arm, (((missing arms))), bad hands,missing fingers,(extradigit),(fewer digits),mutated hands,(fused fingers),(too many fingers),sharp fingers,wrong figernails,long hand,double middle finger,index fingers together,missing indexfinger,interlocked fingers,pieck fingers,sharp fingernails,(steepled fingers),x fingers,((curled fingers)),(no finger gaps),interlocked fingers,fingers different thickness,cross fingers,poor outline,big fingers,finger growth,outline on body,outline on hair,out line on background,more than one hands,fuse arm,fuse elbow,more than two arm,more than two elbow,poorly drawn,bad anatomy,bad,blurry,text,missing fingers,low quality,error,signature,normal quality,cropped,username,watermark,fewer digits,worst quality,extra digit,owres,jpeg artifacts,bad feet,disfigured,long neck,ugly,mutation,malformed,bad proportions,duplicate,font,extra legs,more than 2 nipples,extra limbs,morbid,long body,multiple breasts,liqd,missing limb,cloned face,malformed mutated,mutilated,lowers,ears,futa,face,eyes,tranny,hands,jpeg,mouth,crotch,gap,tentacles,unclear eyes,frame,artifacts,low-quality,extra arms,deformed,mutated,fused anus,artist name,seam,breasts,black tongue,poorly drawn,bad anatomy,bad,blurry,text,missing fingers,low quality,error,signature,normal quality,cropped,username,watermark,fewer digits,worst quality,extra digit,owres,jpeg artifacts,bad feet,disfigured,long neck,ugly,mutation,malformed,bad proportions,duplicate,font,extra legs,more than 2 nipples,extra limbs,morbid,long body,multiple breasts,liqd,missing limb,cloned face,malformed mutated,mutilated,lowers,ears,futa,face,eyes,tranny,hands,jpeg,mouth,crotch,gap,tentacles,unclear eyes,frame,artifacts,low-quality,extra arms,deformed,mutated,fused anus,artist name,seam,breasts,black tongue,more than 2 thighs,Humpbacked,shadow,game,shoes,gloves,animal,worstquality,negative,prompt,fused ears,uncoordinated body,liquid body,fused pussy,bad pussy,bad anus,missing asshole,fused asshole,bad asshole,disappearing legs,disappearing calf,disappearing thigh,disappearing arms,missing hand,fused hand,huge calf,huge thighs,sleeveles,mountain,wort,multiple breasts, {mutated hands and fingers:1.5}, {long body :1.3}, {mutation, poorly drawn :1.2} , black-white, {{bad anatomy}}, liquid body, liquid tongue, {{disfigured}}, malformed, mutated, anatomical nonsense, text font ui, error, malformed hands, {{long neck}}, blurred, lowers, lowres, {{bad anatomy}}, {{bad proportions}}, bad shadow, uncoordinated body, unnatural body, fused breasts, bad breasts, poorly drawn breasts, extra breasts, missing breasts, huge haunch, huge thighs, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, fused ears, bad ears, poorly drawn ears, extra ears, liquid ears, heavy ears, missing ears, fused animal ears, bad animal ears, poorly drawn animal ears, extra animal ears, liquid animal ears, heavy animal ears, missing animal ears, text, ui, error, missing fngers, extra digt, missing fingers, extradigit, missing limb, {fused fingers}, one hand with more than 5 fingers, one hand with less than 5 fingers, one hand with more than 5 digit, one hand with less than 5 digit, extra digit, fewer digits, fused digit, missing digit, bad digit, liquid digit, colorful tongue, black tongue, cropped, wort quality, watermark, username, blurry, JPEG artifacts, signature, 3D, 3D game, 3D game scene, 3D character, malformed feet, extra feet, bad feet, owres, bad anatomy, poorly drawn feet, fused feet, missing feet, extra shoes, bad shoes, fused shoes, more than two shoes, poorly drawn shoes, bad gloves, poorly drawn gloves, fused gloves, bad cum, poorly drawn cum, fused cum, bad hairs, poorly drawn hairs, fused hairs, big muscles, {{ugly}}, bad face, fused face, {{poorly drawn face}}, cloned face, big face, long face, bad eyes, fused eyes poorly drawn eyes, extra eyes, {malformed limbs}, {{extra limbs}}, more than 2 nipples, missing nipples, different nipples, fused nipples, bad nipples, poorly drawn nipples, black nipples, colorful nipples, gross proportions. short arm, (((missing arms))), missing thighs, missing calf, {{missing legs}}, {{mutation}}, duplicate, morbid, mutilated, {{poorly drawn hands}}, more than 1 left hand, more than 1 right hand, {{deformed}}, (blurry), {{disfigured}}, {{more than 2 nipples}}, {{out of frame}}, {{missing legs}}, {{extra arms}}, {too many fingers}, extra thighs, more than 2 thighs, extra calf, fused calf, {{extra legs}}, bad knee, extra knee, more than 2 legs, bad tails, bad mouth, fused mouth, poorly drawn mouth, bad tongue, tongue within mouth, too long tongue, black tongue, big mouth, cracked mouth, bad mouth, dirty face, dirty teeth, dirty pantie, fused pantie, poorly drawn pantie, fused cloth, poorly drawn cloth, bad pantie, yellow teeth, thick lips, bad cameltoe, colorful cameltoe, bad asshole, poorly drawn asshole, fused asshole, missing asshole, bad anus, bad pussy, bad crotch, bad crotch seam, fused anus, fused pussy, fused anus, fused crotch, poorly drawn crotch, fused seam, poorly drawn anus, poorly drawn pussy, poorly drawn crotch, poorly drawn crotch seam, bad thigh gap, missing thigh gap, fused thigh gap, liquid thigh gap, poorly drawn thigh gap, poorly drawn anus, bad collarbone, fused collarbone, missing collarbone, liquid collarbone, strong girl, obesity, worst quality, low quality, normal quality, liquid tentacles, bad tentacles, poorly drawn tentacles, split tentacles, fused tentacles, missing clit, bad clit, fused clit, colorful clit, black clit, liquid clit, QR code, bar code, censored, safety panties, safety knickers, beard, furry ,pony, {pubic hair}, mosaic, excrement, faeces, shit, futa,, panties, thong, fundoshi"
#negative_prompt : str = "((poorly drawn hands)),(((multiple views)))more than 1 left hand, more than 1 right hand, short arm, (((missing arms))), bad hands,missing fingers,(extradigit),(fewer digits),mutated hands,(fused fingers),(too many fingers),sharp fingers,wrong figernails,long hand,double middle finger,index fingers together,missing indexfinger,interlocked fingers,pieck fingers,sharp fingernails,(steepled fingers),x fingers,((curled fingers)),(no finger gaps),interlocked fingers,fingers different thickness,cross fingers,poor outline,big fingers,finger growth,outline on body,outline on hair,out line on background,more than one hands,fuse arm,fuse elbow,more than two arm,more than two elbow,poorly drawn,bad anatomy,bad,blurry,text,missing fingers,low quality,error,signature,normal quality,cropped,username,watermark,fewer digits,worst quality,extra digit,owres,jpeg artifacts,bad feet,disfigured,long neck,ugly,mutation,malformed,bad proportions,duplicate,font,extra legs,more than 2 nipples,extra limbs,morbid,long body,multiple breasts,liqd,missing limb,cloned face,malformed mutated,mutilated,lowers,ears,futa,face,eyes,tranny,hands,jpeg,mouth,crotch,gap,tentacles,unclear eyes,frame,artifacts,low-quality,extra arms,mutated,fused anus,artist name,seam,black tongue,poorly drawn,bad anatomy,bad,blurry,text,missing fingers,low quality,error,signature,normal quality,cropped,username,watermark,fewer digits,worst quality,extra digit,owres,jpeg artifacts,bad feet,disfigured,long neck,ugly,mutation,malformed,bad proportions,duplicate,font,extra legs,more than 2 nipples,extra limbs,morbid,long body,multiple breasts,liqd,missing limb,cloned face,malformed mutated,mutilated,lowers,futa,tranny,jpeg,gap,tentacles,unclear eyes,frame,artifacts,low-quality,extra arms,mutated,fused anus,artist name,seam,breasts,black tongue,more than 2 thighs,Humpbacked,shadow,game,shoes,gloves,animal,worstquality,negative,prompt,fused ears,uncoordinated body,liquid body,fused pussy,bad pussy,bad anus,missing asshole,fused asshole,bad asshole,disappearing legs,disappearing calf,disappearing thigh,disappearing arms,missing hand,fused hand,huge calf,huge thighs,sleeveles,mountain,wort,multiple breasts, {mutated hands and fingers:1.5}, {long body :1.3}, {mutation, poorly drawn :1.2} , black-white, {{bad anatomy}}, liquid body, liquid tongue, {{disfigured}}, malformed, mutated, anatomical nonsense, text font ui, error, malformed hands, {{long neck}}, blurred, lowers, lowres, {{bad anatomy}}, {{bad proportions}}, bad shadow, uncoordinated body, unnatural body, fused breasts, bad breasts, poorly drawn breasts, extra breasts, missing breasts, huge haunch, huge thighs, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, fused ears, bad ears, poorly drawn ears, extra ears, liquid ears, heavy ears, missing ears, fused animal ears, bad animal ears, poorly drawn animal ears, extra animal ears, liquid animal ears, heavy animal ears, missing animal ears, text, ui, error, missing fngers, extra digt, missing fingers, extradigit, missing limb, {fused fingers}, one hand with more than 5 fingers, one hand with less than 5 fingers, one hand with more than 5 digit, one hand with less than 5 digit, extra digit, fewer digits, fused digit, missing digit, bad digit, liquid digit, colorful tongue, black tongue, cropped, wort quality, watermark, username, blurry, JPEG artifacts, signature, 3D, 3D game, 3D game scene, 3D character, malformed feet, extra feet, bad feet, owres, bad anatomy, poorly drawn feet, fused feet, missing feet, extra shoes, bad shoes, fused shoes, more than two shoes, poorly drawn shoes, bad gloves, poorly drawn gloves, fused gloves, bad cum, poorly drawn cum, fused cum, bad hairs, poorly drawn hairs, fused hairs, big muscles, {{ugly}}, bad face, fused face, {{poorly drawn face}}, cloned face, big face, long face, bad eyes, fused eyes poorly drawn eyes, extra eyes, {malformed limbs}, {{extra limbs}}, more than 2 nipples, missing nipples, different nipples, fused nipples, bad nipples, poorly drawn nipples, black nipples, colorful nipples, gross proportions. short arm, (((missing arms))), missing thighs, missing calf, {{missing legs}}, {{mutation}}, duplicate, morbid, mutilated, {{poorly drawn hands}}, more than 1 left hand, more than 1 right hand, {{deformed}}, (blurry), {{disfigured}}, {{more than 2 nipples}}, {{out of frame}}, {{missing legs}}, {{extra arms}}, {too many fingers}, extra thighs, more than 2 thighs, extra calf, fused calf, {{extra legs}}, bad knee, extra knee, more than 2 legs, bad tails, bad mouth, fused mouth, poorly drawn mouth, bad tongue, tongue within mouth, too long tongue, black tongue, big mouth, cracked mouth, bad mouth, dirty face, dirty teeth, dirty pantie, fused pantie, poorly drawn pantie, fused cloth, poorly drawn cloth, bad pantie, yellow teeth, thick lips, bad cameltoe, colorful cameltoe, bad asshole, poorly drawn asshole, fused asshole, missing asshole, bad anus, bad pussy, bad crotch, bad crotch seam, fused anus, fused pussy, fused anus, fused crotch, poorly drawn crotch, fused seam, poorly drawn anus, poorly drawn pussy, poorly drawn crotch, poorly drawn crotch seam, bad thigh gap, missing thigh gap, fused thigh gap, liquid thigh gap, poorly drawn thigh gap, poorly drawn anus, bad collarbone, fused collarbone, missing collarbone, liquid collarbone, strong girl, obesity, worst quality, low quality, normal quality, liquid tentacles, bad tentacles, poorly drawn tentacles, split tentacles, fused tentacles, missing clit, bad clit, fused clit, colorful clit, black clit, liquid clit, QR code, bar code, censored, safety panties, safety knickers, beard, furry ,pony, {pubic hair}, mosaic, excrement, faeces, shit, futa, thong, fundoshi"
negative_prompt : str = "(EasyNegative:1.3), (big muscles:1.2), (censored:1.3), (huge breasts:1.2), pointy ears"
