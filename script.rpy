define liz = Character("Elizabeth", what_slow_cps=25)
define mc = Character (" ", what_slow_cps=25)
define nar = Character(None, kind=nvl, 
    what_slow_cps=25,
    what_slow_abortable=True
)
define narc = Character(None, kind=nvl,
    what_xpos=990,
    what_ypos=540,
    what_xalign=0.5,
    what_textalign=0.5,
    what_slow_cps=25,
    what_slow_abortable=True
)
define Nnar = Character(
    "", window_style="Nnar_window"
    )

transform position:
    zoom 0
    xalign 0.5
    yalign 1.0
    yoffset 950
    on show:
        alpha 0.0
        ease 0.3 alpha 1.0

label start:
##INTRO----------------------------------------------------------------
    scene Bus_Home with dissolve

    nar "Lethargy"
    nar "It consumed every bone in her body"
    nar "The cushion comforted her lightly"
    nar "Yet, still, the pain in her body prevailed"
    nvl clear
    nar "Her eyes were open, yet she saw nothing"
    nar "The cold-conditioned winds kissed her skin, yet she felt nothing"
    nar "She tried desperately to look for comfort, yet she found nothing"
    nar "She stared into something and nothing, all at once"
    nvl clear
    nar "Every breath was bated by exhaustion"
    nar "Every movement congeals her position, bit by bit"
    nar "Every murmur felt like the spear of Spartans down her ears"
    nar "Every touch of light burned the skin of her corneas"
    nvl clear
    nar "She was fighting a battle she couldn't win"
    nar "As much she could try, as desperate as she was"
    nar "No amount of will could ever drag her into slumber"
    nar "Knowingly in vein, she closed her eyes for a moment"
    nvl clear
    scene Old_School with dissolve
    nar "The tranquil breeze of the midday weather..."
    nar "The soothing chatter of children in the playground..."
    nar "The vibrant verdance of Mother nature who embraced every corner of the eye..."
    nar "...The last moment she felt any sense of peace"
    nvl clear
    nar "Whatever happened to satisfaction?..."
    nar "Whatever happened to exhiliration?..."
    nar "When was the last time she enjoyed the warmth of the sun?..."
    nar "When was the last time she saw those she loved?... "
    nvl clear
    scene Home_Night with dissolve
    nar "She used to favor the night for its sunless stillness"
    nar "It always made her treasure the world and all of the evils it holds"
    nar "She walks to the front door. The same one that greets her with a solemn smile at the end of every night"
    nar "And she felt nothing..."
    nvl clear
    scene Room_Night with dissolve
    nar "Begrudgingly, she took a bath..."
    nar "The weight on her skin was relieved, but that one of her heart lingered deeply"
    nar "Hot water...cold water...warm water"
    nar "She turned the knob in many directions, and found her chest weighing the same..."
    nvl clear
    scene Night_Kitchen with dissolve
    nar "She soon dried her hair, then indolently scraps something to eat..."
    nar "Powderized drinks with caffiene riddled her cupboards"
    nar "The cabinets smelled like insect excrement; the only thing filled the empty shelves..."
    nar "The stovetop was clean as crystal, just like the day it was bought..."
    nvl clear
    nar "Some old stale bread was lying on the empty tabletop..."
    nar "Leftovers from a night unknown sat deserted in the fridge..."
    nar "A singular plastic cup with dried saliva sat next to the sink..."
    nar "...good enough..."
    nvl clear
    scene empty with dissolve
    nar "Was that even dinner...?"
    nar "Did her body even notice something enter its walls...?"
    nar "Where did the water go when she drank it...?"
    nar "When did she go bed...?"
    nvl clear
    nar "..."
    nar "......"
    nar "........."
    nar "............"
    nvl clear
    narc "I am sick of this..."
    nvl clear
    narc "I am sick of life..."
    nvl clear
    narc "I am sick of me..."
    nvl clear
    narc "What happened...?"
    nvl clear
    narc "I used to enjoy things..."
    nvl clear
    narc "I used to cherish my life..."
    nvl clear
    narc "I used see the world through gleaming stars and brilliant hope"
    nvl clear
    narc "Where did it all go...?"
    nvl clear
    narc "Was it me...?"
    nvl clear
    narc "Did I do something wrong...?"
    nvl clear
    narc "Did I insult some higher being...?"
    nvl clear
    narc "Please forgive me, whatever you are..."
    nvl clear
    narc ".............................."
    nvl clear
    narc "I wish my life didn't have to be this way..."
    nvl clear
    narc "I wish my nights weren't like this..."
    nvl clear
    narc "I wish my days weren't like this..."
    nvl clear
    narc ".............................."
    nvl clear
    narc "I want to be somewhere else..."
    nvl clear
    narc "I want to be someone else..."
    nvl clear 
    narc "With a different life..."
    nvl clear
    narc "...a different face..."
    nvl clear
    narc "...a different time..."
    nvl clear
    narc "Whoever's listening..."
    nvl clear
    narc "...please..."
    nvl clear
    narc "........."
    nvl clear

##SCENE1-MANIFESTATION----------------------------------------------
    scene Mirror_Chamber with dissolve

    Nnar "test1"
    Nnar "test2"
    Nnar "test3"
    
    show Liz_Idle_DormU_HD_Angry_combi at position

    liz "Good morning!" 

    show Liz_Idle_DormU_HD_SmileOB_combi at position
    hide Liz_Idle_DormU_HU_SmileCB_combi
    with dissolve

    liz "I hope you slept well in your room last night ^^"

    show Liz_Idle_DormU_HD_SmileOECM_combi at position
    hide Liz_Idle_DormU_HD_SmileOB_combi
    with dissolve


    liz "I'm sorry about Riddle yesterday, he tends to act like that sometimes..."

    return