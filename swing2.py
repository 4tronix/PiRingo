# Example Python code for PiRingo
#
# Expands are of lit LEDs clockwise or anticlockwise following press of switches
# If all LEDS are lit the Left player or Right player wins
# Switch1 moves anti-clockwise, Switch2 moves clockwise
# Must be run as root - sudo python swing2.py 

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

# Set all LEDs between activeLED and 0 to be ON. All others to be OFF
# activeLED can be from -11 to +11
def lightLEDs(activeLED):
  a = 0
  while a < NUMLEDS:
    if ((a == 0) or ((activeLED >= 0) and (a <= activeLED)) or ((activeLED < 0) and (a > (11 + activeLED)))):
      GPIO.output(LEDS[a],LEDON)
    else:
      GPIO.output(LEDS[a],LEDOFF)
    a += 1

# Function to switch all LEDs OFF
def alloff ():
    for val in LEDS:
        GPIO.output(val,LEDOFF)

# Flash the Right side LEDs for winner
def flashRight(val):
    alloff()
    while (val > 0):
        lightLEDs(6)
        time.sleep (0.2)
        alloff()
        time.sleep(0.2)
        val -= 1

# Flash the Left side LEDs for winner
def flashLeft(val):
    alloff()
    while (val > 0):
        lightLEDs(-6)
        time.sleep (0.2)
        alloff()
        time.sleep(0.2)
        val -= 1

# Run the GPIO initialisation function
setupgpio()

# Start with LED1 ON and all others OFF
lightLEDs (myLED)

print "Press Ctrl-C to exit"
while (myLED > -11 and myLED < 12):
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
  lightLEDs (myLED)
if myLED == 12: # Right player Wins
    flashRight(10)
else:
    flashLeft(10) # Left player wins

GPIO.cleanup()
