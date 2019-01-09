# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:42:44 2018

@author: Harsha
"""

import os
#from record import record_to_file
import sounddevice as sd
import soundfile as sf
from ASR import ASR
samplerate = 44100  # Hertz
duration = 3  # seconds
#filename = 'output.wav'

def register_speaker(path):
    #path="C:\\Users\\Ramesh\\Desktop\\College Stuff\\7th Sem stuff\\Project\\Speaker\\Train1\\"
    id1=input('Enter your ID: ')
    try:
        os.mkdir(path+'S'+id1)
    except FileExistsError:
        print("ID Already Exists, Enter unique ID")
        id1=input('Enter your ID: ')
        pass
    finally:
        os.chdir(path+'S'+id1)
#x=1
    for i in range(5):
        a=input('Press Enter to record')
        mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                        channels=1, blocking=True)
        sf.write('S'+id1+str(i)+'.wav', mydata, samplerate)
if __name__ =="__main__":
    path="C:\\Users\\Ramesh\\Desktop\\College Stuff\\7th Sem stuff\\Project\\Speaker\\Train1\\"
    register_speaker(path)
    print("Recording Done!   Thank You!")
    ASR()

