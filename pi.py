#!/usr/bin/env python
import sys
import time
import os
import serial
from microbitdongle import Dongle

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
    "l0": "bc",  # base clockwise
    "r0": "bac", # base anti clockwise
    "l1": "go",  # grip open
    "r1": "gc",  # grip close
    "d0": "su",  # shoulder up
    "u0": "sd",  # shoulder down
    "u1": "wd",  # wrist down
    "d1": "wu",  # wrist up
    "d2": "eu",  # elbow up
    "u2": "ed",  # elbow down
    "f": None
    }
mb = Dongle(debug=True)

while True:
    data = mb.recv()
    if data:
        print(data)
        if data in dir_to_move:
            d = dir_to_move[data]
        else:
            d = dir_to_move[data[0]]
        if d:
            c = smoves[d]
            print(d, c)
            r.MoveArm(t=0.25, cmd=c)
