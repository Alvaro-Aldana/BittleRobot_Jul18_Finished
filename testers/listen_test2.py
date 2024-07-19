import sounddevice as sd
from scipy.io.wavfile import write,read
import speech_recognition as sr
r = sr.Recognizer()

fs=44100 
sd.default.samplerate = fs
second=5 # how long the recording is
print("recording")
record_voice=sd.rec(int(second*fs),samplerate=fs,channels=1)
sd.wait()
write("output.wav",fs,record_voice)
sample_rate,data = read("output.wav")

print("playing")
sd.play(data)
sd.wait()