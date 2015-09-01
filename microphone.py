#!/usr/bin/env python

import spidev.SpiDev as SpiDev 
import time

s = SpiDev()
s.open(0,0)

INPUT = 24

print "Listening for sound"

print s.ReadChannel()

while GPIO.input(INPUT) == 0:
    motion_detected = time.time()

print "Motion detected at ", motion_detected

GPIO.cleanup()

