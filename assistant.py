import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import wolframalpha
import random
import os

var = pyttsx3.init('sapi5')
audio = var.getProperty('voices')
var.setProperty('voice', audio[1].id)

def speak(param):
    var.say(param)
    var.runAndWait()

def Initial():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('Hi, My name is siri, How may i help you')

def fun():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('Listening...') 
        print('Listening...')
        r.energy_threshold = 500
        r.pause_threshold = 0.5
        param = r.listen(source)

    try:
        speak('Recognizing...')
        print('Recognizing...')
        voice = r.recognize_google(param,language='en-in')
        print(f'User Said : {voice}\n')
        speak(f'User Said : {voice}\n')
    
    except Exception as e:
        print('Speak Again Please!')
        speak('Speak Again Please!')
        return 'None'
    return voice

if __name__ == "__main__":
    Initial()
    while True:
        voice = fun().lower()
        if 'wikipedia' in voice:
            speak('Searching...')
            voice = voice.replace('wikipedia','')
            speak('According to Wkipedia')
            result = wikipedia.summary(voice, sentences=2)
            print(result)
            speak(result)

        elif 'hi' in voice:
            speak('Hi, How can I help you')

        elif 'how are you' in voice or 'kaisi' in voice:
            print('I am doing great,What can I help you with?')
            speak('I am doing great,What can I help you with?')
        
        elif 'open youtube' in voice:
            webbrowser.open('youtube.com')

        # elif 'open google' in voice:
        #     webbrowser.open('google.com')
            

        elif 'open music' in voice or 'play music' in voice:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            index = 0
            os.startfile(os.path.join(music_dir, songs[index]))
            speak('Playing')
            speak(songs[index])

        elif 'stop' in voice:
            os.system("taskkill /im vlc.exe")
            speak('Music Player has been stopped')
            
        elif 'next' in voice:
            index += 1
            os.startfile(os.path.join(music_dir, songs[index]))
            speak('Playing')
            speak(songs[index])

        elif 'time' in voice:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            speak(f'The time is {time}')
            

        elif 'vs code' in voice:
            speak('Opening visual studio code')
            path = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'who are you' in voice or 'define yourself' in voice:
            speak('''Hello, I am Person. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra''')

        elif 'who created you' in voice or 'who made you' in voice:
            speak('I have been created by Suraj Patil')

        elif 'google' in voice:
            index1 = voice.split().index('google')
            voice1 = voice.split()[index1+1:]
            str1 = ''
            for i in voice1:
                str1+=i
            speak('Searching...')
            webbrowser.open('https://www.google.com/search?q=' + str1)

        elif 'calculate' in voice:
            try:
                index2 = voice.split().index('calculate')
                voice2 = voice.split()[index2+1:]
                client = wolframalpha.Client('V2Q8TJ-6RRG2V7YQG')
                res = client.voice(' '.join(voice2))
                output = next(res.results).text
                print('Answer is : ',output)
                speak(f'Answer is {output}')
            except:
                print('Speak Again Please')
                speak('Speak Again Please')

        elif 'thank you' in voice or 'shukriya' in voice or 'dhanyawad' in voice:
            speak('Its my pleasure!')

        elif 'quit' in voice or 'band' in voice:
            speak('Thank you for using me')
            exit()