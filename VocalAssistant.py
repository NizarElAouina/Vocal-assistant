"""
Created on Tue Feb 21 08:25:39 2023

@author: nizar
"""

"""
import speech_recognition as sr
import openai
import pyaudio
import smtplib
import pywhatkit
import datetime
import subprocess
import webbrowser
import pyttsx3
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
  """
import speech_recognition as sr
from gtts import gTTS
import os
import datetime

# create a recognizer object
r = sr.Recognizer()

while True:
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        if "quit" in text:
            print("Quitting the program...")
            break
        elif "time" in text or "hour" in text:
            now = datetime.datetime.now()

            # convert the current time to a string
            time_str = now.strftime("%I:%M %p")
        
            # define the text you want to convert to speech
            text = "The time is " + time_str
            
            print(text)
            
            # create an instance of gTTS class
            tts = gTTS(text=text, lang='en')
    
            # save the audio file
            tts.save("time.mp3")
    
            # play the audio file
            os.system("mpg321 time.mp3")
        else:
            print("Sorry, I didn't understand what you said.")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
