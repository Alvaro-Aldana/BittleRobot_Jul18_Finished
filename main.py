# main code with serial connection and the main loop

import time
import speaker
import serial
import listener
import textAnalyzer
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "quit"
CONNECTED = True
ser = serial.Serial(port="/dev/cu.Petoi-30AD", baudrate = 115200)



def main():
    speaker.speak("connecting")
    print(listener.translator.translate("if nothing is printing after this quit the code and check the connection of the robot"))
    #setting up serial connection FIX: how would i make this better
    while True:
        robot_msg = ser.readline()
        print(robot_msg)
        if robot_msg == b'd\r\n' or b'?\r\n':
            break
    speaker.speak("Finished Connection")


def loop():
    global CONNECTED
    speaker.speak(f"current langauge is {listener.lang.value}, you can change the language by saying 'ingles', or 'spanish'")
    while CONNECTED:
        # asks the user for a command
        user_msg = listener.listening()
        if user_msg == "quit":
            CONNECTED = False
        else:
            # it takes what is said and until it can figure out a command it stays here
            user_msgs = textAnalyzer.analyze(user_msg)
            print(user_msgs)
            for i in range(len(user_msgs)):
                print(user_msgs[i][0])
                if user_msgs[i][0] == "quit":
                    CONNECTED = False
                else:
                    # makes the text into byte
                    message = user_msgs[i][0].encode(FORMAT)
                    # sends the byte to the robot
                    ser.write(message)
                    if len(user_msgs[i])>1:
                        time.sleep(int(user_msgs[i][1]))
                        ser.write("kup".encode(FORMAT))
                        time.sleep(0.1)
                    elif i<len(user_msgs):
                        time.sleep(5)
    # if quit the connection gets closed
    speaker.speak(listener.translator.translate("closing connection"))
    ser.write("krest".encode(FORMAT))
    ser.close()

# code that runs
main()
loop()

