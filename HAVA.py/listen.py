#importing speech recognition so that ai can recognize the speech

import speech_recognition as sr 

#making a fuction to make ai constantly listen
 
def listen():
    r = sr.Recognizer()  #call recognizer function
    with sr.Microphone() as source:  #takes voice from microphone as source
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)  #every 2 sec computer recognizes

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  #uses google tts
        print(f'You said: {query}')
    except:
        return ''

    query = str(query)
    return query.lower()

def WakeUp():
    query = Listen()


