#!/usr/bin/python
#\file    libaictrl1.py
#\brief   Library for AI-based robot control experiment-1.
#\author  Akihiko Yamaguchi, info@akihikoy.net
#\version 0.1
#\date    Aug.28, 2018

import sys,os
sys.path.append('../finger' if os.path.dirname(__file__)=='' else os.path.dirname(__file__)+'/../finger')
from dynamixel_lib import *
from libaictrl2 import *
import random, math
import time

#Parameters
P_START= 2100

#Setup the finger robot:
def SetupRobot():
  dxl= TDynamixel1('XM430-W350', '/dev/ttyUSB0')
  dxl.Setup()
  dxl.EnableTorque()
  return dxl

#Move to initial position
def MoveToInit(dxl):
  dxl.MoveTo(P_START, blocking=True)
  time.sleep(0.1)  #wait 0.5 sec
  print 'Current position=',dxl.Position()

#Move to a target position
def MoveToTrg(dxl, d_angle, effort):
  p_trg= dxl.InvConvPos( dxl.ConvPos(P_START)-d_angle )
  pwm= int(effort*dxl.MAX_PWM)
  print P_START, p_trg, pwm
  dxl.SetPWM(pwm)
  dxl.MoveTo(p_trg, blocking=True)
  #dxl.MoveToC(p_trg,current)
  time.sleep(0.1)  #wait 0.1 sec
  print 'Current position=',dxl.Position()

if __name__=='__main__':
  #Finger robot test:
  dxl= SetupRobot()
  MoveToInit(dxl)
  MoveToTrg(dxl, 0.2, 1.0)
  raw_input('Waiting a key: ')
  MoveToTrg(dxl, 0.8, 0.7)

