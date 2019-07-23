#!/usr/bin/env python

from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0,7)
c = random.randint(0,255)

sense.set_pixel(r,r,(c,c,c))
time.sleep(3)
sense.clear()
