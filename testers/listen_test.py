import sounddevice
from scipy.io.wavfile import write



fs=44100 
second=5 # how long the recording is
sounddevice.default.dtype='int32'
print("recording")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=1)
sounddevice.wait()
write("output.wav",fs,record_voice)

import speech_recognition as sr
r = sr.Recognizer()

jackhammer = sr.AudioFile("output.wav")
with jackhammer as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))