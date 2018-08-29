#!/usr/bin/python
#Optimizing policy with CMA-ES

# Importing often-used libraries...
import sys
sys.path.append('../finger')
sys.path.append('../sample')
from dynamixel_lib import *
import cma
import time

#Setup the device
dxl= TDynamixel1('XM430-W350')
dxl.Setup()
dxl.EnableTorque()

# Objective function to be minimized (parameter x[0] is initial position)
def f(x):
  #Move to initial position
  p_start= x[0]
  dxl.MoveTo(p_start)
  time.sleep(0.1)  #wait 0.1 sec
  raw_input('Press enter to throw: ')

  #Move to a target position
  p_trg= p_start-400
  dxl.MoveTo(p_trg)
  time.sleep(0.1)  #wait 0.1 sec
  dist= raw_input('Type the distance ("" or "none" for invalid experiment): ')
  if dist in ('','none'):  return None
  dist= float(dist)  #Convert to a floating point value
  #For logging:
  print x[0], dist
  return -dist

# Run CMA-ES to minimize the function f
res= cma.fmin(f,[2000],100.0,{'verb_log':0,'popsize':4})

print res
print 'Result=',res[0]

