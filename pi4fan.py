#!/usr/bin/env python3
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
pin = 18 # Which GPIO pin are you connected to?
maxTMP = 50 # Max temp in C to turn on the fan
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        fanON()
    else:
        fanOFF()
    return()
def setPin(mode): 
    GPIO.output(pin, mode)
    return()
try:
    setup() 
    while True:
        getTEMP()
    sleep(10) # Read the temperature every 10 sec
except KeyboardInterrupt:  
    GPIO.cleanup()