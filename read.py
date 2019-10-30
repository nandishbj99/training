#import sys
#sys.path.append('/usr/local/lib/python2.7/dist-packages/')
from gtts import gTTS 
from playsound import playsound
import os
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["avi"]

GPIO.setwarnings(False)
reader=SimpleMFRC522()
def texttospeech(mytext):
    
    language = 'en' 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("address.mp3") 
    os.system("address.mp3") 
    playsound("/home/address.mp3")






try:
    time.sleep(1)
    id,text=reader.read()
    #print(id)
    #print(text)
    t="12.55N,77.30E"
    m=text.split()
    
    mytable=mydb['table']
    data=mydb.table.find_one({"tagname":m[0]})
    texttospeech(data['addressaudio'])
    
    
    
        
finally:
    GPIO.cleanup()