# Example Python code for PiRingo
#
# Makes the PiRingo into a clock
# This code does not use any control loops for simplicity of understanding
# Must be run as root - sudo python clock.py 

# Set up the necessary libraries
import time, RPi.GPIO as GPIO
# Ignore GPIO warnings that may be due to earlier programs
GPIO.setwarnings(False)

# Tell GPIO library to use physical GPIO connector pins
GPIO.setmode(GPIO.BOARD)

# Setup all the LED pins as Ouputs
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

cleanup = (True)
while (cleanup == True):
    GPIO.output(7, 1)
    GPIO.output(11, 1)
    GPIO.output(12, 1)
    GPIO.output(13, 1)
    GPIO.output(15, 1)
    GPIO.output(16, 1)
    GPIO.output(18, 1)
    GPIO.output(22, 1)
    GPIO.output(24, 1)
    GPIO.output(26, 1)
    GPIO.output(8, 1)
    GPIO.output(10, 1)

    cleanup = (False)
print " Clock is running !"
#GPIO.cleanup()
def Blink(numTimes,speed,pin):
    for i in range(0,numTimes):## Run loop numTimes
        GPIO.output(pin,True)## Switch on pin 7
        time.sleep(speed)## Wait
        GPIO.output(pin,False)## Switch off pin 7
        time.sleep(speed)## Wait
    GPIO.output(pin,False)

try:
    running = (True)
    hour =  int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    iterations = 30
    speed = 2
    while (running == True):
        hour =  int(time.strftime("%I"))
        minute = int(time.strftime("%M"))
        print (hour,minute)
        print 
        
        
        if hour == 1:
            GPIO.output(7, 1) #12 o'clock
            GPIO.output(11, 0)#1 o'clock
            
        elif hour == 2:
            GPIO.output(11, 1)
            GPIO.output(12, 0)
            
        elif hour == 3:
            GPIO.output(12, 1)
            GPIO.output(13, 0)
        elif hour == 4:
            GPIO.output(13, 1)
            GPIO.output(15, 0)
        elif hour == 5:
            GPIO.output(15, 1)
            GPIO.output(16, 0)
        elif hour == 6:
            GPIO.output(16, 1)
            GPIO.output(18, 0)
        elif hour == 7:
            GPIO.output(18, 1)
            GPIO.output(22, 0)
        elif hour == 8:
            GPIO.output(22, 1)
            GPIO.output(24, 0)
        elif hour == 9:
            GPIO.output(24, 1)
            GPIO.output(26, 0)
        elif hour == 10:
            GPIO.output(26, 1)
            GPIO.output(8, 0)
        elif hour == 11:
            GPIO.output(8, 1)
            GPIO.output(10, 0)    
        elif hour == 12:
            GPIO.output(7, 0)
            GPIO.output(10, 1)    
        else:
            print " It`s broken"
        

        if minute == 5:
            Blink(int(iterations),float(speed),11)
            GPIO.output(7, 1)
            GPIO.output(11, 1)
        elif minute == 10:
            Blink(int(iterations),float(speed),12)
            GPIO.output(11, 1)
            GPIO.output(12, 1)
        elif minute == 15:
            Blink(int(iterations),float(speed),13)
            GPIO.output(12, 1)
            GPIO.output(13, 1)
        elif minute == 20:
            Blink(int(iterations),float(speed),15)
            GPIO.output(13, 1)
            GPIO.output(15, 1)
        elif minute == 25:
            Blink(int(iterations),float(speed),16)
            GPIO.output(15, 1)
            GPIO.output(16, 1)
        elif minute == 30:
            Blink(int(iterations),float(speed),18)
            GPIO.output(16, 1)
            GPIO.output(18, 1)
        elif minute == 35:
            Blink(int(iterations),float(speed),22)
            GPIO.output(18, 1)
            GPIO.output(22, 1)
        elif minute == 40:
            Blink(int(iterations),float(speed),24)
            GPIO.output(22, 1)
            GPIO.output(24, 1)
        elif minute == 45:
            Blink(int(iterations),float(speed),26)
            GPIO.output(24, 1)
            GPIO.output(26, 1)
        elif minute == 50:
            Blink(int(iterations),float(speed),8)
            GPIO.output(26, 1)
            GPIO.output(8, 1)
        elif minute == 55:
            Blink(int(iterations),float(speed),10)
            GPIO.output(8, 1)
            GPIO.output(10, 1)
        elif minute == 0:
            Blink(int(iterations),float(speed),7)
            GPIO.output(10, 1)
            GPIO.output(7, 1)
        else:
            print "not in a five minute range"
        time.sleep(60)

       
except KeyboardInterrupt:
        GPIO.cleanup()
        print (" Hope you had fun ")     

