# listens for the users command
# turns user speech into text
# and selects the langauge

import speaker
import speech_recognition as speechrecog
from enum import Enum
from nltk.tokenize import word_tokenize
import variables
from translate import Translator
recog = speechrecog.Recognizer()
import sounddevice
from scipy.io.wavfile import write
import threading
import time

fs=44100 
second=5 # how long the recording is
sounddevice.default.dtype='int32' # sound device and speech_recognition do not use the same default data type

class language(Enum):
     ENGLISH = "en-US"
     SPANISH = "es-ES"

# change the language here
lang = language.ENGLISH
waiting = True
if lang == language.ENGLISH:
    translator= Translator(to_lang='en',from_lang='en')
else:
    translator= Translator(to_lang='es',from_lang='en')

def askForCommand():
    #return input("listening... ")
    # asking the microphone for audio data
    speaker.speak("listening...")
    record_voice()
    text = read_wav()
    speaker.speak(translator.translate("Text: ")+text)
    # checking if needs to change the langauge
    return change_language(text)


def change_language(text):
    words = word_tokenize(text)
    # if you want to change the language you can
    # if the langauge is changed the robot will ask for instructions
    global lang, translator
    for word in words:
        if word=="inglés":
                lang = language.ENGLISH
                speaker.speak("cambiando el idioma a ingles")
                translator= Translator(to_lang='en',from_lang='en')
                return askForCommand()
        if word=="spanish":
                lang = language.SPANISH
                speaker.speak("changing the language to spanish")
                translator= Translator(to_lang='es',from_lang='en')
                return askForCommand()
    return text



def listening():
    #return input("listening...")
    global waiting
    waiting = True
    speaker.speak(translator.translate("say hey Google or listen to initiate command"))
    x =threading.Thread(target=listen_in_back)
    x.start()
    while waiting:
        print(".") # DO NOT ADD end= to the print statement, for some reason it crashes it
        record_voice()
    return askForCommand()


def listen_in_back():
    time.sleep(6)
    global waiting
    while waiting:
        message = read_wav()
        words = word_tokenize(message)
        for text in words:
            if text == "listen" or "google" or "escucha":
                waiting = False


def record_voice():
    record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=1)
    sounddevice.wait()
    write("audio.wav",fs,record_voice)

def read_wav():
    with speechrecog.AudioFile("audio.wav") as source:
        audio = recog.record(source)
    try:
        text = recog.recognize_google(audio)
        text = text.lower()
        print(text)
        return text
    except Exception as e:
        print("..")
    return ""
