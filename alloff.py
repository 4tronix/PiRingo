# Example Python code for PiRingo
#
# Turns all LEDs OFF
# This code does not use any control loops for simplicity of understanding
# Must be run as root - sudo python alloff.py 

# set up the necessary libraries
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

# Now switch all the LEDs ON (0 = ON, 1 = OFF)
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

