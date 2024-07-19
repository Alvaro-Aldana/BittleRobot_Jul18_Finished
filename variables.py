
# you write down all the parameters necessary
# at the end of the list for each action is the command
english_actions = [
    ["quit","quit"],
    # Walking actions (3)
    ["walk","forward","kwkF"], 
    ["walk","right","kwkR"], 
    ["walk","left","kwkL"], 
# (walk) backwards actions (3)
    ["backward","kbk"], 
    ["backward","left","kbkL"], 
    ["backward","right","kbkR"], 
# crawling actions (3)
    ["crawl","forward","kcrF"], 
    ["crawl","right","kcrR"], 
    ["crawl","left","kcrL"], 
# pushing actions (3)
    ["push","forward","kphF"], 
    ["push","right","kphR"], 
    ["push","left","kphL"], 
# running actions (3)
    ["run","forward","ktrF"], 
    ["run","right","ktrR"], 
    ["run","left","ktrL"], 
# hop and spin (3)
    ["hop","kbdF"],
    ["spin","right","kvtL"],
    ["spin","left","kvtR"],
# hands (3)
    ["handstand","khds"],
    ["wave","khi"],
    ["hand","shake","khsk"],
# pushups (2)
# FIX: recognize_google sees audio of pushups as push-ups and recgonize_sphinx sees pushups as pushups
    ["one","hand","pushups","kpu1"],
    ["pushups","kpu"],
# the rest (12)
    ["lay","down","krest"],
    ["butt","up","kbuttUp"],
    ["stand","up","kup"],
    ["come","here","kcmh"],
    ["high","five","kfiv"],

    ["good","boy","kgdb"],
    ["hand","up","khu"], # hands 
    ["play","dead","kpd"],
    ["flip","over","krc"],
    ["shake","head","kwh"],

    ["back","foot","up","klifted"], # feet
    ["calibration","mode","kcalib"],
    ["roll","over","krl"],
# signles
    ["balance","kbalance"],
    ["bow","kdropped"],
    ["crouch","klnd"],
    ["sit","ksit"],
    ["stretch","kstr"],

    ["zero","kzero"],
    ["stomp","kvtF"],
    ["angry","kang"],
    ["backflip","kbf"],
    ["fight","kbx"],

    ["cheer","kchr"],
    ["look","kck"],
    ["dig","kdg"],
    ["hug","khg"],
    ["jump","kjmp"],

    ["kick","kkc"],
    ["nod","knd"],
    ["pee","kpee"],
    ["scratch","kscrh"],
    ["sniff","ksnf"],

    ["flat","ktbl"],
    ["test","kts"],
    ["moonwalk","kmn"],
]
#
##
###########################################################################################################
##
#
#
##
###########################################################################################################
##
#
spanish_actions = [
    # Walking actions (3)
    ["andar","forward","kwkF"], 
    ["andar","derecha","kwkR"], 
    ["andar","izquierda","kwkL"], 
# (walk) backwards actions (3)
    ["backward","kbk"], 
    ["backward","izquierda","kbkL"], 
    ["backward","derecha","kbkR"], 
# crawling actions (3)
    ["gatear","forward","kcrF"], 
    ["gatear","derecha","kcrR"], 
    ["gatear","izquierda","kcrL"], 
# pushing actions (3)
    ["empujar","forward","kphF"], 
    ["empujar","derecha","kphR"], 
    ["empujar","izquierda","kphL"], 
    ["","",""], 
# running actions (3)
    ["correr","forward","ktrF"], 
    ["correr","izquierda","ktrR"], 
    ["correr","derecha","ktrL"], 
# hop and spin (3)
    ["hop","kbdF"],
    ["spin","derecha","kvtL"], # gira o girar
    ["spin","izquierda","kvtR"],
# hands (3)
    ["pino","khds"],
    ["saludo","khi"],
    ["hand","shake","khsk"], # dame la mano?
# pushups (2)
    ["one","hand","push","up","kpu1"], # que es push ups en espanol?
    ["push-ups","kpu"],
# the rest (12)
    ["lay","down","krest"], # ????
    ["culo","arriba","kbuttUp"],
    ["levantar","kup"], # ???
    ["ven","aqui","kcmh"], # ???
    ["chocar","cinco","kfiv"],

    ["buen","chico","kgdb"],
    ["mano","arriba","khu"], # hands 
    ["juega","muerto","kpd"],
    ["espalda","krc"], # ???
    ["agitar","cabeza","kwh"], # ????

    ["pata","trasero","arriba","klifted"], # feet
    ["modo","calibra","kcalib"],
    ["date","vueta","krl"],
# signles
    ["equilibrio","kbalance"],
    ["bow","kdropped"], #???
    ["agachar","klnd"],
    ["sentar","ksit"],
    ["estirar","kstr"],

    ["cero","kzero"],
    ["pisotear","kvtF"],
    ["enfadado","kang"],
    ["voltereto","kbf"], # voltereta
    ["pelea","kbx"],

    ["salud","kchr"],
    ["mirar","kck"],
    ["excava","kdg"],
    ["abrazo","khg"],
    ["salta","kjmp"],

    ["patado","kkc"],
    ["nod","knd"], #???
    ["pis","kpee"],
    ["rascar","kscrh"],
    ["sniff","ksnf"], #???

    ["mesa","ktbl"],
    ["test","kts"],
    ["caminata","lunar","kmn"],
]
#
##
###########################################################################################################
##
#
#
##
###########################################################################################################
##
#

actions = []

def make_spanish_main():
    global actions
    actions = spanish_actions
def make_english_main():
    global actions
    actions = english_actions

actions = english_actions