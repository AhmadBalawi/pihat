#!/usr/bin/env python
#this script defines colors for sensehat on text
from sense_hat import SenseHat
sense = SenseHat()

#use RGB values to define the freaking colors
red = (255,0,0)
green = (0,255,0)

speed = 0.005

message = "THIS SENSEHAT IS CURSED. CEASE USE IMMEDIATELY."

sense.show_message(message, speed, text_colour=red, back_colour=green)

sense.clear()
