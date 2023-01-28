#importing python speech to text module

import pyttsx3


#making a function to speak
def speak(Text):
    print('   ')
    engine = pyttsx3.init('sapi5')  #microsoft speaking api
    voices = engine.getProperty('voices') #saving available voices to voices variable
    engine.setProperty('voices', voices[0].id)  #setting the voice we want to use
    engine.setProperty('rate', 170)  #setting voice speed
    print(f'A.I : {Text}')
    engine.say(text=Text)    #speaks what is text
    engine.runAndWait()
    print('    ')
