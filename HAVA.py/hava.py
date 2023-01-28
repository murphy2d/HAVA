import random
import json
import torch
from brain import NeuralNetwork
from neuralNet import bag_of_words, tokenize
import serial
import time

device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
with open('Python Projects\HAVA.py\intents.json','r') as json_data:
    intents = json.load(json_data)

FILE = "Python Projects\\HAVA.py\\trainData.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


#-------------


Name = 'HAVA'
from listen import listen
from Speak import speak
from function import NonInputExecution
from function import InputExecution

def Main():
    
    sentence = listen()
    result = str(sentence)

    
    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)

    _ , predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent['responses'])

                if 'time' in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "day" in reply:
                    NonInputExecution(reply)
                elif "outro" in intent['tag']:
                    NonInputExecution(tag)
                elif "wikipedia" in reply:
                    InputExecution(reply, sentence)
                elif "google" in reply:
                    InputExecution(reply, result)
                elif "OpenDoor" in intent['tag']:
                    NonInputExecution(tag)
                elif "CloseDoor" in intent['tag']:
                    NonInputExecution(tag)
                elif "HallLightOpen" in intent['tag']:
                    NonInputExecution(tag)
                elif "HallLightClose" in intent['tag']:
                    NonInputExecution(tag)
                elif "RoomLightOpen" in intent['tag']:
                    NonInputExecution(tag)
                elif "RoomLightClose" in intent['tag']:
                    NonInputExecution(tag)
                elif "SocketOn" in intent['tag']:
                    NonInputExecution(tag)
                elif "SocketOff" in intent['tag']:
                    NonInputExecution(tag)
                elif "GarageDoorOn" in intent['tag']:
                    NonInputExecution(tag)
                elif "GarageDoorOff" in intent['tag']:
                    NonInputExecution(tag)
                

                else:
                    speak(reply)
while True:
    Main()
