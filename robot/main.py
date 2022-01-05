#!/usr/bin/env pybricks-micropython


# Execute with brickrun -r pybricks-micropython -- main.py

import socket
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
import sys

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=265)
colorSensor = ColorSensor(Port.S1)

while True:
    sleep(0.2)
    ambient = colorSensor.ambient()
    action = None
    if ambient < 2:
        action = 'none'
    elif ambient < 3:
        action = 'left'
    elif ambient < 6:
        action = 'backward'
    elif ambient < 9:
        action = 'forward'
    elif ambient < 11:
        action = 'right'
    if action == 'forward':
        robot.straight(200)
    elif action == 'backward':
        robot.straight(-200)
    elif action == 'left':
        robot.turn(30)
    elif action == 'right':
        robot.turn(-30)
