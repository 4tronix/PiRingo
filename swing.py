# Example Python code for PiRingo
#
# Moves a single LED clockwise or anticlockwise following press of switches
# Switch1 moves anti-clockwise, Switch2 moves clockwise
# Must be run as root - sudo python swing.py 

# Set up the necessary libraries
import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Ignore GPIO warnings that may be due to earlier programs
GPIO.setwarnings(False)

# Tell GPIO library to use physical GPIO connector pins
GPIO.setmode(GPIO.BOARD)

# Define pins to use for switches and LEDs
SWITCH1_PIN = 19
SWITCH2_PIN = 21
LEDS = [7, 11, 12, 13, 15, 16, 18, 22, 24, 26, 8, 10]

# Define value to use for LEDs ON and OFF states
LEDOFF = 1
LEDON = 0
NUMLEDS = 12

# Function to initialise all GPIO pins
# Set up all LED pins as outputs
# Set up both Switches as Inputs with pullup resistors
def setupgpio():
    a = 0
    while a < NUMLEDS:
        GPIO.setup(LEDS[a], GPIO.OUT)
        a += 1
    GPIO.setup(SWITCH1_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH2_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Initialise stored values of switches (for edge-detection in software)
switch1 = False
switch2 = False

# Define currently active LED. 0 = LED1, 11 = LED12
myLED = 0

# Set the active LED to be ON, all others to be OFF
def lightLEDs(led):
  a = 0
  while a < NUMLEDS:
    if (a == led):
      GPIO.output(LEDS[a],LEDON)
    else:
      GPIO.output(LEDS[a],LEDOFF)
    a += 1

# Run the GPIO initialisation function
setupgpio()

# Start with LED1 ON and all others OFF
lightLEDs (myLED)

print "Press Ctrl-C to exit"
while True:
  if (GPIO.input(SWITCH1_PIN) == 0) :
    if (not switch1):
      myLED -= 1 # Only gets here when Wwitch1 is first pressed (edge detected)
    switch1 = True
  else:
    switch1 = False
  if (GPIO.input(SWITCH2_PIN) == 0) :
    if (not switch2):
      myLED += 1 # Only gets here when Wwitch2 is first pressed (edge detected)
    switch2 = True
  else:
    switch2 = False
  if myLED < 0:
    myLED = 11 # revert to LED12 if go "below" LED1
  if myLED > 11:
    myLED = 0 # revert to LED1 if go "above" LED12
  lightLEDs (myLED)

GPIO.cleanup()
