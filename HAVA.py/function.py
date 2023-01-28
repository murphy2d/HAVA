#We will have two function. Non input and input. when we say time, date etc it is a command that is input but if google search hava will have to input value for the output

import datetime
from Speak import speak
import wikipedia
import pywhatkit
import json
import random
import serial
import time
# from hava import Main

# serialcomm = serial.Serial('COM7', 115200)

# serialcomm.timeout = 1

with open('Python Projects\HAVA.py\intents.json','r') as json_data:
    intents = json.load(json_data)

def Time():
    time = datetime.datetime.now().strftime("%H : %M")
    speak(f"The time is {time}")

def Date():
    date = datetime.date.today()
    speak(f"Today's date is {date}")

def Day():
    day = datetime.datetime.now().strftime("%A")
    speak(f"It's {day} today")

def Exit():
    for intent in intents['intents']:
        if "outro" in intent['tag']:
            outro = random.choice(intent['responses'])
            speak(outro)
            exit()

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()

    elif "day" in query:
        Day()
    
    elif "outro" in query:
        Exit()

    # elif "OpenDoor" in query:
    #     i = b'0'
    #     for intent in intents['intents']:
    #         if "OpenDoor" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    #     # serialcomm.close()

    # elif "CloseDoor" in query:
    #     i = b'1'
    #     for intent in intents['intents']:
    #         if "CloseDoor" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    #     # serialcomm.close()
    # elif "GarageDoorOn" in query:
    #     i = b'2'
    #     for intent in intents['intents']:
    #         if "GarageDoorOn" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    #     # serialcomm.close()
    # elif "GarageDoorOff" in query:
    #     i = b'3'
    #     for intent in intents['intents']:
    #         if "GarageDoorOff" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    #     # serialcomm.close()

    # elif "HallLightOpen" in query:
    #     i = b'i'
    #     for intent in intents['intents']:
    #         if "OpenLight" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    # elif "HallLightClose" in query:
    #     i = b'h'
    #     for intent in intents['intents']:
    #         if "CloseLight" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    # elif "RoomLightOpen" in query:
    #     i = b's'
    #     for intent in intents['intents']:
    #         if "RoomLightOpen" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    # elif "RoomLightClose" in query:
    #     i = b'r'
    #     for intent in intents['intents']:
    #         if "RoomLightClose" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    # elif "SocketOn" in query:
    #     i = b'u'
    #     for intent in intents['intents']:
    #         if "SocketOn" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)
    # elif "SocketOff" in query:
    #     i = b't'
    #     for intent in intents['intents']:
    #         if "RoomLightClose" in intent['tag']:
    #             speak(intent['responses'])
    #     serialcomm.write(i)
    #     time.sleep(0.5)


def InputExecution(tag, query):
    if "wikipedia" in tag:
        try:
            name = str(query).replace("who is","").replace("about", "").replace("what is", "").replace("wikipedia", "").replace("do you know about", "").replace("tell me about", "").replace("what do you know about", "").replace("give information about", "").replace("can you tell me about", "")
            result = wikipedia.summary(name, sentences=2)
            speak(result)
        except:
            pass

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        query = query.replace("google search", "")
        pywhatkit.search(query)

    