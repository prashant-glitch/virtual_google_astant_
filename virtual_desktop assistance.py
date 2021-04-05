
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
i=0
listner=sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[i].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.......")
            voice=listner.listen(source)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('palyingsong' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%P')
        talk('current time is'+time)
    elif 'who the heck in command':
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date ' in command:
        talk('sorry, I have a hedache')
    elif 'are you single'in command:
        talk('i am in relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again')

while True:
    run_alexa()
        
        
        
        
        
