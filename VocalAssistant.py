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

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    if "what time is it" in text:
        # get the current time
        now = datetime.datetime.now()

        # convert the current time to a string
        time_str = now.strftime("%I:%M %p")

        # define the text you want to convert to speech
        text = "The time is " + time_str

        # create an
          
            
            
