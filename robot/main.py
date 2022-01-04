#!/usr/bin/env pybricks-micropython
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
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
colorSensor = ColorSensor(Port.S1)

colorActionMap = {
    Color.RED: 'forward',
    Color.BLUE: 'backward',
    Color.GREEN: 'left',
    Color.YELLOW: 'right',
}

while True:
    color = colorSensor.color()
    if color in colorActionMap:
        action = colorActionMap[color]
        if action == 'forward':
            robot.straight(100)
        elif action == 'backward':
            robot.straight(-100)
        elif action == 'left':
            robot.turn(30)
        elif action == 'right':
            robot.turn(-30)
