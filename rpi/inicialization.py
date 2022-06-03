#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Moves selected servo to 90° position

import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

pca = ServoKit(channels=16)

i = 15
pca.servo[i].set_pulse_width_range(500, 2400)
pca.servo[i].angle = 80
time.sleep(1)
pca.servo[i].angle = 100
time.sleep(1)
pca.servo[i].angle = 90
time.sleep(1)
pca.servo[i].angle = None
