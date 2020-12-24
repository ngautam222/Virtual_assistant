import time
from datetime import datetime
from time import ctime
import webbrowser
import playsound
import os
import random
import pywhatkit
import requests
from gtts import gTTS
import wikipedia
import pyjokes
import speech_recognition as sr
import subprocess
import datetime

r = sr.Recognizer()
wake = False

def wakeWord():
    with sr.Microphone() as source:
        # print("say something")
        #print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=2)
        vc = ""
        try:
            vc = r.recognize_google(audio)
        except sr.UnknownValueError:
            print()

    return vc


def record_audio():
    with sr.Microphone() as source:
        # print("say something")
        #print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=2)
        vc = ""
        try:
            vc = r.recognize_google(audio)
        except sr.UnknownValueError:
            print()


    return vc
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome! Please tell me how may I help you")


def respond(phrase):
    if 'name' in phrase:
        speak("hello there my name is olivia")
    if 'time' in phrase:
        speak(ctime())
    if 'search' in phrase:
        speak("What do you want to search ?")
        search = record_audio()
        print(search)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak("i found this")
    if 'find location' in phrase:
        speak("What location ?")
        lo = record_audio()
        print(lo)
        url = 'https://google.nl/maps/place/' + lo + '/&amp;'
        webbrowser.get().open(url)
        speak("i found this")
    if 'exit' in phrase:
        speak('See you soon!')
        exit()
    if 'play' in phrase:
        speak("What would you like to play")
        song = record_audio()
        speak("Playing" + song)
        pywhatkit.playonyt(song)
    if 'who' in phrase or 'what is'in phrase:
        query = phrase.replace('who is', '')
        info = wikipedia.summary(query, 2)
        print(info)
        speak(info)
    if 'joke' in phrase:
        speak(pyjokes.get_joke())
    if 'open Safari' in phrase:
        speak("opening safari")
        subprocess.call(["Safari.exe"])
    if 'stop listening' in phrase:
        speak("OK")
        time.sleep(15)
    if 'write a note' in phrase:
        speak("what should i write sir?")
        note = record_audio()
        file = open('nick.txt', 'w')
        file.write(note)
        speak("done!")
    if 'open note' in phrase:
        speak("opening master")
        file = open("nick.txt", 'r')
        print(file.read())

    if 'how are you' in phrase or 'how you doing' in phrase or 'hows it going' in phrase:
        speak("I am feeling very well ,thank you!")
    else:
        speak("could you repeat that?")
        speak("call my name again and i may respond!")


def speak(audio_String):
    tts = gTTS(text=audio_String, lang='en-uk',slow= False)
    r = random.randint(1, 100000)
    audio_file = 'audio-' + str(r) + 'mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_String)
    os.remove(audio_file)


while True:
   # wishMe()
    vc = wakeWord()
    if 'Olivia' in vc:
        speak("I am listening!")
        vc = record_audio()
        print(vc)
        respond(vc)
