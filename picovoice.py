import pyaudio
p=pyaudio.PyAudio()
for i in range(9): 
    print(p.get_device_info_by_index(i))







import pvporcupine
import struct
import speech_recognition as sr
import pyttsx3
import webbrowser
import random
import requests
from bs4 import BeautifulSoup
import logging
import time
from phue import Bridge
import json
import pyjokes

import os
import keyboard

print(("""\

        ██▀▀▀      ▄▄▄            ██▀███        ██▒   █▓      ██▓       ██████      
       ▒██        ▒████▄         ▓██ ▒ ██▒     ▓██░   █▒     ▓██▒     ▒██    ▒      
       ░██        ▒██  ▀█▄       ▓██ ░▄█ ▒      ▓██  █▒░     ▒██▒     ░ ▓██▄        
    ▓██▄██▓       ░██▄▄▄▄██      ▒██▀▀█▄         ▒██ █░░     ░██░       ▒   ██▒     
     ▓███▒    ██▓  ▓█   ▓██▒ ██▓ ░██▓ ▒██▒ ██▓    ▒▀█░   ██▓ ░██░ ██▓ ▒██████▒▒ ██▓ 
     ▒▓▒▒░    ▒▓▒  ▒▒   ▓▒█░ ▒▓▒ ░ ▒▓ ░▒▓░ ▒▓▒    ░ ▐░   ▒▓▒ ░▓   ▒▓▒ ▒ ▒▓▒ ▒ ░ ▒▓▒ 
     ▒ ░▒░    ░▒    ▒   ▒▒ ░ ░▒    ░▒ ░ ▒░ ░▒     ░ ░░   ░▒   ▒ ░ ░▒  ░ ░▒  ░ ░ ░▒  
     ░ ░ ░    ░     ░   ▒    ░     ░░   ░  ░        ░░   ░    ▒ ░ ░   ░  ░  ░   ░   
     ░   ░     ░        ░  ░  ░     ░       ░        ░    ░   ░    ░        ░    ░  
               ░              ░             ░       ░     ░        ░             ░  """))

# -------------------- Setup -------------------

ACCESS_KEY = "xHJTZXeeTD4qh30L9hR2rQw/1NJL05mZT66O63rptiohbqQ8wwUslw=="

r = sr.Recognizer()
engine = pyttsx3.init()


API_KEY = "NF16xKntnYza-6BO9sLEQ1-xERuNL14aQ6DbNgCB"





def takeCommand(conv_type):
    if conv_type == "s":
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.7
            audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-US")
                print(f"You said: {query}\n")

            except Exception as e:
                print(e)
                print("Sorry, I did not understand what you said.")
                return "None"
            return query
    elif conv_type == "w":
        time.sleep(0.5)
        query = input('Command: ')
        return query

# -------------- Initializing Wake Word Detection ---------------

def main():
    porcupine = None
    pa = None
    audio_stream = None
    
    try:
        #porcupine = pvporcupine.create(access_key=ACCESS_KEY,keyword_paths=['سلام-حافظ_fa_windows_v2_2_0.ppn'],
        #  model_path='porcupine_params_fa.pv')
        porcupine = pvporcupine.create(access_key=ACCESS_KEY,keywords=['hey google','bumblebee'])
        
        
        pa = pyaudio.PyAudio()
        print(porcupine.sample_rate)
        audio_stream = pa.open(
            
            rate=16000,#44100,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)
        while True:
            pcm = audio_stream.read(porcupine.frame_length,exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            keyword_index = porcupine.process(pcm)
            if keyword_index == 0:
                print("و علیکم سلام")
                #Conversation("s")
                time.sleep(1)
                #print("Awaiting your call "+USER)
            if keyword_index == 1:
                print("سوال بپرس")
                #Conversation("s")
                time.sleep(1)
                #print("Awaiting your call "+USER)
            if keyword_index == 2:
                print('هرهرهر')
                #Conversation("s")
                time.sleep(1)
                #print("Awaiting your call "+USER)
            elif keyboard.is_pressed('q'):
                print("Detected")
                #Conversation("w")
                time.sleep(1)
                #print("Awaiting your call "+USER)
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()
            
            
main()
