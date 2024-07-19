# analyzes the user message and decodes it into commands that the robot can follow


import variables
import time
import speaker
from nltk.tokenize import word_tokenize
# using lemmatizing
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import listener
from deep_translator import GoogleTranslator



complete_actions = []
incomplete_action = []

# MAIN FUNCTION
def analyze(text):
    global complete_actions
    complete_actions= []
    return search(analyze_text(text))

# use keywords to find out what the user wants the dog to do
def analyze_text(text):
    global complete_actions,incomplete_action
    # translates to english
    if listener.lang.value == "es-ES":
        text = GoogleTranslator(source='spanish', target='english').translate(text)
    # splits up the text into single words
    words = word_tokenize(text)
    for i in range(len(words)):
        words[i]=lemmatizer.lemmatize(words[i],"v")
        if words[i]=="leave":
            words[i]="left"
        print(words[i],end="")
    return words  


# FIX: the ungliest part of the code
# searches through a list of already tolkenized and lemmantized words to see if there are any matches
def search(words):
    global incomplete_action,complete_actions
# IMPORTANT: this is only for the start, to know if it starts with command or parameter.
# goes through the whole list of word deleting words[0] as it goes
    while len(words)>0:
        if words[0].isdigit() and len(incomplete_action)==0:
            if len(complete_actions)>0:
                complete_actions[len(complete_actions)-1].append(words[0])
        else:
# is it command parameter or neither?
            a=-1
            while a<len(variables.actions)-1:
                a+=1
                # is it parameter
                if len(incomplete_action)>0: #is there a command to fill with paramters
                    # FIX: currently it will add the parameter to the command only if the command is equal, not the rest of the parameters
                    if incomplete_action[0]==variables.actions[a][0]: # is this the right command
                        if words[0]==variables.actions[a][len(incomplete_action)]: # is this the right parameter
                            parameter_sequence(words[0])
                            # check if action is complete
                            check_if_complete(a)
                            # reset
                            a=len(variables.actions)-1
            # is it command
                if words[0]==variables.actions[a][0]:
                    command_sequence(words[0])
                    # check if action is complete
                    check_if_complete(a)
                    a=len(variables.actions)-1
        words.pop(0)
        print(words)

    print(f"incomplete_action: {incomplete_action}")
# if command is not found it asks again
    if len(complete_actions)>0:
        return complete_actions
    speaker.speak(listener.translator.translate("more information needed to complete an action"))
    time.sleep(2)
    #return analyze(input("comand:"))
    return analyze(listener.askForCommand())




# given a command, it wipes the spot of incomplete commands and makes a new one
def command_sequence(text):
    global incomplete_action
    if len(incomplete_action)>0:
        ask_for_parameter()
        incomplete_action = []
    incomplete_action.append(text)

# whatever command is in the base this parameter gets added to it
def parameter_sequence(text):
    global incomplete_action
    incomplete_action.append(text)
    print(incomplete_action)

# after adding a command or parameter checks if all parameters are filled
def check_if_complete(action_num):
    global incomplete_action,complete_actions
    if len(incomplete_action)==len(variables.actions[action_num])-1:
        complete_actions.append([variables.actions[action_num][len(incomplete_action)]])
        incomplete_action = []




# making sure you want to delete a command
def ask_for_parameter():
    global incomplete_action,complete_actions
    speaker.speak(f"this command will be overwritten, do you want to complete the incomplete action {incomplete_action}?")
    #text = input()
    text = listener.askForCommand()
    words = word_tokenize(text)
    again = True
    for w in words:
        if w=="yes":
            speaker.speak("listening...")
            #paramter_search(input())
            paramter_search(listener.askForCommand())
            again = False
        if w=="no":
            again = False
            speaker.speak("overwriting command")
    if again:
        ask_for_parameter()


# if incomplete action wants to be completed this will be called
def paramter_search(text):
    global incomplete_action,complete_actions
    words = analyze_text(text)
    while len(words)>0:
# is it command parameter or neither?
        a=-1
        while a<len(variables.actions)-1:
            a+=1
            # is it parameter
            # FIX: currently it will add the parameter to the command only if the command is equal, not the rest of the parameters
            if incomplete_action[0]==variables.actions[a][0]: # is this the right command
                if words[0]==variables.actions[a][len(incomplete_action)]: # is this the right parameter
                    parameter_sequence(words[0])
                    # check if action is complete
                    check_if_complete(a)
                    # reset
                    a=len(variables.actions)-1
        words.pop(0)
        print(words)
    if len(incomplete_action)==0:
        pass
    else:
        speaker.speak("incorrect parameters given")
        ask_for_parameter()

