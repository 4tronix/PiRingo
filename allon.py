# Example Python code for PiRingo
#
# Turns all LEDs ON
# This code does not use any control loops for simplicity of understanding
# Must be run as root - sudo python allon.py 

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

# Now switch all the LEDs ON (0 = ON, 1 = OFF)
GPIO.output(7, 0)
GPIO.output(11, 0)
GPIO.output(12, 0)
GPIO.output(13, 0)
GPIO.output(15, 0)
GPIO.output(16, 0)
GPIO.output(18, 0)
GPIO.output(22, 0)
GPIO.output(24, 0)
GPIO.output(26, 0)
GPIO.output(8, 0)
GPIO.output(10, 0)


