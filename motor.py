#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

motorPins = [18,23,25,12]
on = GPIO.HIGH
off = GPIO.LOW
delay = 0.003
fullStep = [[on,on,off,off],[off,on,on,off],[off,off,on,on],[on,off,off,on]]
lotsStep = [[on,on,on,off],[off,on,on,on],[on,off,on,on],[on,on,off,on]]
halfStep = [[on,off,off,off],[off,on,off,off],[off,off,on,off],[off,off,off,on]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPins, GPIO.OUT)

print "Motoring..."

try:
        while True:
                for step in range(len(fullStep)):
                        GPIO.output(motorPins, fullStep[step])
                        time.sleep(delay)
except KeyboardInterrupt:
        pass

print "BBBYYYEEE"
GPIO.output(motorPins, off)

GPIO.cleanup()

