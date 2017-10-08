import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Declare LED locations
led = 4 # blue
led1 = 5 # green
led2 = 18 # white
led3 = 25 # red

GPIO.setwarnings(False)
# Setup pins
def setupPins():
    print("setup pins")
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(led2,GPIO.OUT)
    GPIO.setup(led3,GPIO.OUT)
    return
# turn on LED
def turnOn():
    print("LED on")
    GPIO.output(led,GPIO.HIGH)
    GPIO.output(led1,GPIO.HIGH)
    GPIO.output(led2,GPIO.HIGH)
    GPIO.output(led3,GPIO.HIGH)
# turn off LED
def turnOff():
    print("LED off")
    GPIO.output(led,GPIO.LOW)
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2,GPIO.LOW)
    GPIO.output(led3,GPIO.LOW)
setupPins()
turnOn()
time.sleep(5) # wait 5 seconds and turn the leds off
turnOff()