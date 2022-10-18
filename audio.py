import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 180)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Jervis' in command:
                command = command.replace('Jervis', '')
                print(command)
    except:
        pass
    return command


def run_Ai():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who are you' in command:
        talk("I am Your Artificial Slave ")
    elif 'how are you' in command:
        talk("I am Fine How about you ")
    elif 'i am sad' in command:
        talk("Don't Worry I always with you ")
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    else:
        talk('Please say the command again.')


while True:
    run_Ai()