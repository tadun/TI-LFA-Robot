#!/usr/bin/env python

import time
import brickpi3 
import sys

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
time.sleep(0.11)

try:
	if len(sys.argv) != 2 :
		print("Please enter a valid command.")
	else:
		print "cable" ,sys.argv[1]
		value = BP.get_sensor(BP.PORT_1)
		print "Touch sensor:", (value)	
		try:
			if sys.argv[1]== 'in':
				if value==0:
					print("Connecting...")        			
					BP.set_motor_position(BP.PORT_A, 0)
				if value==1:
					print("Already connected.")
	
			elif sys.argv[1]== 'out':
				if value==0:
					print("Already disconnected.")
				if value==1:
					print("Disconnecting...")
					BP.set_motor_position(BP.PORT_A, 180)
  
			else:
				print("Error (unknown command)")

		except brickpi3.SensorError as error:
					print(error)
	
		time.sleep(0.02)

except KeyboardInterrupt:
	BP.reset_all()
