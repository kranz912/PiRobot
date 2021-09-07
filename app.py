#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
import random
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])
from ezblock import delay
from ezblock import Ultrasonic
from ezblock import Pin

reference = 10

distance = 99

pin_D0 = Pin("D0")

pin_D1 = Pin("D1")

reference = None

turn = None

turn = ['turn left', 'turn right', 'stop']


def forever():

    global reference, distance
    distance = Ultrasonic(pin_D0, pin_D1).read()

    global turn
    if distance >= reference:
        __SLOTH__.do_action(random.choice(turn), (random.randint(2, 7)), 100)
        __SLOTH__.do_action('forward', (random.randint(4, 7)), 100)
        __SLOTH__.do_action('stop', 1, 100)
        delay((random.randint(4, 15) * 100))
    else:
        __SLOTH__.do_action('backward', 1, 100)
        __SLOTH__.do_action('stop', 1, 100)
        __SLOTH__.do_action('turn right', 1, 100)
        __SLOTH__.do_action('stop', 1, 100)

if __name__ == "__main__":
    while True:
        forever()  