#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

INPUT = 23

print "Looking for motion"

GPIO.setup(INPUT, GPIO.IN)

while GPIO.input(INPUT) == 0:
        motion_detected = time.time()

print "Motion detected at ", motion_detected

GPIO.cleanup()


