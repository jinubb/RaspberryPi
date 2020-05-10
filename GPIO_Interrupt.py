#!/usr/bin/env python
 
import RPi.GPIO as GPIO 

print GPIO.VERSION

GPIO.setmode(GPIO.BCM) 
 

GPIO.setup(4, GPIO.IN) 
globalCounter = 0 
 

def myInterrupt(channel): 
    global globalCounter 
    globalCounter += 1
    print " Done. counter:" , globalCounter
 
 

GPIO.add_event_detect(4, GPIO.FALLING, callback=myInterrupt) 
 
try: 
    raw_input("Press Enter to Exit\n>") 
except KeyboardInterrupt: 
    GPIO.cleanup() # clean up GPIO on CTRL+C exit 
    GPIO.remove_event_detect(4) 
 
GPIO.remove_event_detect(4) 
GPIO.cleanup() # clean up GPIO on normal exit
