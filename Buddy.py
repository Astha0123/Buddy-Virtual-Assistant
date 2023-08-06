import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
# engine.say('  hi. I  am  your  fellow ')
# engine.say('  How  may  I  help  you. ')
#engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print ('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buddy' in command:
                command = command.replace('buddy','')
                print(command)
    except:
        pass 
    return command

def run_fellow():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play' , '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'search' in  command:
        person = command.replace('search' ,'')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'are you single' in command:
        talk('I am in the relationship with  Wifi')


    elif 'joke'  in command:
        talk(pyjokes.get_joke())

    else:
        talk('Could not catch you! Please repeat again.')



while True:
   run_fellow()
