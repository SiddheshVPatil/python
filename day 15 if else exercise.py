#python exercise 
# good morning sir 

import time
import pyttsx3
engine = pyttsx3.init()
# engine.say("hello")
timeset=int(input("Enter time"))
ti=time.strftime('%H:%M:%S')
ti=int(time.strftime('%H'))

if(ti<=12):
    engine.say("good morning sir!!!")
elif(ti<=18):
    engine.say("good afternoon sir!!!")
else:
    engine.say("good night sir!!!")
if(ti==timeset):
    engine.say("wake up sid!!!")
else:
    engine.say("Soja raja!!!")
engine.runAndWait()

    
    


    
    


