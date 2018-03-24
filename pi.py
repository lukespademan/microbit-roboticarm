#!/usr/bin/env python
import sys
import time
import os
import serial

#import the maplinrobot class
from maplinrobot import MaplinRobot


r = MaplinRobot()
smoves = {}
for m in r.moves:
  print(m)
  a = m.split("-")
  a = [b[0] for b in a]
  a = "".join(a)
  smoves[a] = m

smoves["lo"] = "light-on"
dir_to_move = {
    "l": "bc",
    "r": "bac",
    "d0": "su",
    "u0": "sd",
    "u1": "wd",
    "d1": "wu",
    "f": None
    }
print(smoves)

PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE


while True:
    data = s.readline().decode("UTF-8").rstrip()
    if data:
        print(data, end="")
        if data in dir_to_move:
            d = dir_to_move[data]
        else:
            d = dir_to_move[data[0]]
        if d:
            c = smoves[d]
            print(d, c)
            r.MoveArm(t=0.25, cmd=c)
