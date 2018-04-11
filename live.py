#!/usr/bin/env python
import sys
import time
import os


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
print(smoves)
while True:
    #c = smoves["sd"]
    #r.MoveArm(t=0.5, cmd=c)
    #c = smoves["su"]
    #r.MoveArm(t=0.5, cmd=c)



    cmd = input("Command: ").split(" ")
    c = smoves[cmd[0]]
    r.MoveArm(t=float(cmd[1]), cmd=c)
