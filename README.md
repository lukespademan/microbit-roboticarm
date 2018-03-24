# Microbit Roboticarm
This allows you to control the maplin robotic arm with two microbits and a raspberrypi

It currenly supports: Base rotation, Shouler movement

## maplinrobot.py
taken from the magpi? (i think). This file is imported by pi.py and comminucates with the robotic arm

## pi.py
this takes the data from a microbit (microbitdongle.py) which it commmunicates with over serial, and uses maplinrobot.py to move the robot

## microbitdongle.py
connected to the pi via serial. takes data revieved from radio and sends it over serial

## controller.py
the user tilts this to choose a direction. An arrow is showing on the screen. The data is sent over radio to the microdongle.
