# all things printed on the terminal will be spoken through here

from os import system
import time


def speak(text):
    print(text)
    try:
        system("say {}".format(text))
        time.sleep(len(text)/20)
        pass
    except:
        pass

