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
colorSensor = ColorSensor(Port.S2)
left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=265)
robot.settings(
    straight_speed=500,
    straight_acceleration=100,
    turn_rate=300,
    turn_acceleration=100
)
ev3.speaker.beep()
nSamples = 10

# fd = open('/tmp/debug.log', 'w')

while True:
    # sleep(0.5)
    ambient = 0
    for i in range(nSamples):
        ambient += colorSensor.ambient()
        sleep(0.05)
    ambient /= nSamples
    # print('New iteration', file=fd)
    # print([ambient], file=fd)
    action = 'none'
    if ambient >= 4.0:
        action = 'bell'
    elif ambient >= 2.0:
        action = 'left'
    elif ambient == 1.0:
        action = 'right'
    else:
        action = 'none'
    # print('Action: ' + action, file=fd)
    if action == 'none':
        robot.stop()
    elif action == 'left':
        robot.turn(45)
    elif action == 'right':
        robot.turn(-45)
    elif action == 'bell':
        ev3.speaker.beep()
