#!/usr/bin/env python


import time
import brickpi3

BP = brickpi3.BrickPi3()
i = 0
try:
	while i<100:
		i = i + 1
		print(i)
		BP.set_motor_position(BP.PORT_A, 180)
		time.sleep(0.5)
		print("out")
		BP.set_motor_position(BP.PORT_A, 0)
		print("in")
		time.sleep(0.5)

	time.sleep(0.02)

except KeyboardInterrupt:
    BP.reset_all()
