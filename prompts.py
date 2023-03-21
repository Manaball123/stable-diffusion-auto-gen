from cfgutils import *

positive_prompts : list = [
    #"huge filesize" , 
    #"ultra-detailed", 
    #"highres", 
    #"extremely detailed", 
    "(best quality:1.2)", 
    "(masterpiece:1.2)",
    "(detailed:1.2)"
]


alpha = [
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
    LORA("grabbingOwnAss_v1", 1, bundled_tags = ["grabbing own ass", "ass spread", "ass stretch"])
    ], 1, 1.2, True),
    #["stockings", 1.5]
]


asuka_0 : list = [
    UnmodifiedList(positive_prompts),
    ["nsfw", 0.9, NORAND],
    "sweat",
    "feet",
    "toes",
    RandElement(ElementBundle([
    "cum on body",
    "cum in pussy",
    "cum pool",
    ]), 0.7),
    
    #RandElement("breast out"),
    #["1girl", 1.0, NORAND],
    "pussy",
    #"nipples",
    "puffed nipples",
    ["small breasts", 1.0, NORAND],
    #"skinny",
    RandElement("heavy breathing"),
    "cute",
    #["sex", 1.2],
    RandElement("looking at viewer"),
    "blush",
    "long hair",
    RandElement("open mouth", 0.6),
    "breasts",
    RandElement("naked",0.7),
    RandTable([
    "on side",
    "spread legs",
    "lying",
    LORA("povSquattingCowgirlLora_pscowgirl", 1, bundled_tags = [["squatting cowgirl, cowgirl", 1.2, NORAND]]),
    LORA("grabbingOwnAss_v1", 1, bundled_tags = ["grabbing own ass", "ass spread", "ass stretch"])
    ], 1, 1.2, True),
    #asukaLangleySouryuu_v1
    LORA("asukaLangleySouryuu_v1", 0.8, True, [["souryuu asuka langley",1.0], ["interface headset", 1.0], RandTable(["multicolored bodysuit", "yellow dress"], 1)], [1.2,1.2,1.2,1.2,1.2,1.1,1.1,1.1,0.7,0.6,0.5,0.3,0.3,0.3,0.3,0.3,0.3]),
    RandElement("red footwear", 0.6),
    RandElement("eyepatch", 0.7)
    #["stockings", 1.5]
]

asuka_1 = [
    UnmodifiedList(["((masterpiece,best quality, detailed)), <lora:asukaLangleySouryuu_v1:0.8>, souryuu asuka langley, interface headset, blue choker, yellow dress, red footwear, eyepatch, naked, pussy, cum, cum in pussy"])
]

asuka_neg_1 = "low quality, bad image, poor quality, poor image, jacket, shirt, (sketch by bad-artist-anime:0.9), (painting by bad-artist:0.9), (bad-hands-5-2:0.9), (bad_prompt:0.5), watermark, text, error, blurry, jpeg artifacts, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, artist name, (worst quality, low quality:1.4), bad anatomy, greyscale, monochrome, lowres, bad proportions, bad hands, multiple arms, multiple legs, deformed, text, error, missing fingers, extra fingers, extra digit, extra limb, extra nipple, extra breast, missing limb, floating limbs, disconnected limbs, severed, dismembered, corpse, malformed hands, long neck, long body, fewer digits, deformed, disfigured, amputee, mutated, mutation, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, (((censored))), fat, long body, poorly drawn face, ((futa))"

