#! /usr/bin/env pything
#this scripts shows a scrolling message on pihat
from sense_hat import SenseHat
sense = SenseHat()

#send the text Hello World! to show_message() function
sense.show_message("The Beatles: Rock Band is the best game ever, heck you if you don't think so as well, idiot.")
