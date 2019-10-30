import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gtts import gTTS 
from playsound import playsound 
import os
reader=SimpleMFRC522()
GPIO.setwarnings(False)
try:
    text=input("New data:")
    print("place yuor tag to write")
    reader.write(text)
    print("written")
finally:
    GPIO.cleanup()
    

 
mytext = 'R V CSE Branch'
language = 'en' 
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("welcome.mp3") 
playsound("GIVE PATH")