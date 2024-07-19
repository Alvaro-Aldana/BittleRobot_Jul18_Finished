import speech_recognition as sr
from enum import Enum
recog = sr.Recognizer()

class language(Enum):
     ENGLISH = "en-US"
     SPANISH = "es-ES"
lang = language.ENGLISH
def callback(recognizer, audio):

    try:     
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio,language=lang.value))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()  

with m as source:
        r.adjust_for_ambient_noise(source)
stop_listening = r.listen_in_background(m, callback)

while True:
    if input('unrelated input ...')=="quit":
         break
    

stop_listening()




with sr.Microphone() as source:     
        print("listening...")
        recog.adjust_for_ambient_noise(source, duration=5)
        # implement a hey google type thing to start listening when it hears that
        audioData = recog.listen(source,phrase_time_limit=5)

# checking if recognizable
try:    
        # recognized, turning audio to text
        print("recognizing")

        text = recog.recognize_google(audioData, language=lang.value)
        print(text)
except sr.UnknownValueError:
    print("Google API cannot recognize")
except sr.RequestError as e:
    print("Could not request from Google API; {0}".format(e))