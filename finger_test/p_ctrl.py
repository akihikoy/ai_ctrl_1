#!/usr/bin/python
#Example of P control

#Importing libraries...
import sys
sys.path.append('../finger')
from dynamixel_lib import *
import time
import math
import numpy as np

#Setup the device
dxl= TDynamixel1('XM430-W350')
dxl.Setup()
dxl.EnableTorque()

#Move to initial position
p_start= 2100
dxl.MoveTo(p_start)
time.sleep(2.0)  #wait 2 sec
print 'Current position=',dxl.Position()

tol= 40  #Tolerance
p_trg= 1500  #Target position
k_p= 0.3  #P-gain
while abs(p_trg-dxl.Position()) > tol:
  p_diff= k_p * (p_trg-dxl.Position())
  dxl.MoveTo(dxl.Position()+p_diff, wait=False)
  time.sleep(0.01)
