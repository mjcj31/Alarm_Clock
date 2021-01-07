import sys
import time
import os
import webbrowser


time_input = input("> ")
Time = time.strftime("%H:%M")

while Time != time_input:
    #print("time is " + Time)
    Time = time.strftime("%H:%M")
    #time.sleep(10)

if Time == time_input:
    print("This is working now")
    webbrowser.open('https://en.wikipedia.org/wiki/Main_Page')
