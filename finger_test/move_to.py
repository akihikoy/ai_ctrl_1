#!/usr/bin/python
#Move Dynamixel to the initial position, and to a target

# Importing libraries...
import sys
sys.path.append('../finger')
from dynamixel_lib import *
import time

#Setup the device
dxl= TDynamixel1()
dxl.Setup()

#Move to initial position
p_start= 2300
dxl.MoveTo(p_start)
time.sleep(1.0)  #wait 1 sec
print 'Current position=',dxl.Position()

#Move to a target position
p_trg= p_start-400
dxl.MoveTo(p_trg)
time.sleep(0.1)  #wait 0.1 sec
print 'Current position=',dxl.Position()
