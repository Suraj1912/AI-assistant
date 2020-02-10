import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import wolframalpha
import random
import pygame
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('Hi, My name is David, How may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'User Said : {query}\n')
    
    except Exception as e:
        print('Speak Again Please!')
        speak('Speak Again Please!')
        return 'None'
    return query

if __name__ == "__main__":
    Wish()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia','')
            speak('According to Wkipedia')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open music' in query:
            random1 = random.randint(0,1)
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random1]))

        elif 'stop' in query:
            pygame.mixer.music.stop(random1)


        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {time}')
            print(time)

        elif 'open vscode' in query:
            path = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'who are you' in query or 'define yourself' in query:
            speak('''Hello, I am Person. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra''')

        elif 'who created you' in query or 'who made you' in query:
            speak('I have been created by Suraj Patil')

        elif 'google' in query:
            index1 = query.split().index('google')
            query1 = query.split()[index1+1:]
            str1 = ''
            for i in query1:
                str1+=i
            speak('Searching...')
            webbrowser.open('https://www.google.com/search?q=' + str1)

        elif 'calculate' in query:
            index2 = query.split().index('calculate')
            query2 = query.split()[index2+1:]
            client = wolframalpha.Client('V2Q8TJ-6RRG2V7YQG')
            res = client.query(' '.join(query2))
            output = next(res.results).text
            print(output)
            speak(output)

        elif 'thank you' in query:
            speak('Its my pleasure!')

        elif 'quit' in query:
            speak('Thank you for using me')
            exit()