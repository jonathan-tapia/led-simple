import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Declare LED locations
led1 = 19 # green
led2 = 21 # white

GPIO.setwarnings(False)
# Setup pins
def setupPins():
    print("setup pins")
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(led2,GPIO.OUT)
    return
# turn on LED
def turnOn():
    print("LED on")
    GPIO.output(led1,GPIO.HIGH)
    GPIO.output(led2,GPIO.HIGH)
# turn off LED
def turnOff():
    print("LED off")
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2,GPIO.LOW)
setupPins()
turnOn()
time.sleep(5) # wait 5 seconds and turn the leds off
turnOff()
