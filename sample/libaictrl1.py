#!/usr/bin/python
#\file    libaictrl1.py
#\brief   Library for AI-based robot control experiment-1.
#\author  Akihiko Yamaguchi, info@akihikoy.net
#\version 0.1
#\date    Aug.28, 2018

import sys,os
sys.path.append('../finger' if os.path.dirname(__file__)=='' else os.path.dirname(__file__)+'/../finger')
from dynamixel_lib import *
from libspline import *
from libplot import PlotF
import cma
import random, math
import numpy as np
import time
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.neural_network import MLPRegressor

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

#Train GPR (Gaussian Process for Regression) with data set.
def TrainGPR(data_x, data_y):
  # Training GPR so that GPR can map from x to y.
  # You can play with different kernels.
  ##kernel= C(1.0, (1e-3, 1e3)) * RBF(1.0, (0.1, 10.0))
  #kernel= C(1.0, (1.0, 1.0)) * RBF(1.0, (0.1, 10.0))
  #kernel= C(1.0, (1e-3, 1e3)) * RBF(3.0, (3.0, 3.0))
  #kernel= RBF(1.0, (0.1, 10.0))
  kernel= RBF(1.0, (0.1, 0.1))
  gp= GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
  gp.fit(np.array(data_x).reshape(len(data_x),1), np.array(data_y).reshape(len(data_y),1))
  return lambda x: gp.predict([[x]])[0,0]

#Train MLP (Multilayer Perceptron) for regression with data set.
def TrainMLPR(data_x, data_y):
  # Training MLP (Multilayer Perceptron for Regression) so that MLP can map from x to y.
  mlpreg= MLPRegressor(activation='relu', hidden_layer_sizes=(20, 20), solver='adam', tol=1e-6, alpha=0.01, max_iter=200000, random_state=2)
  mlpreg.fit(np.array(data_x).reshape(len(data_x),1), data_y)
  return lambda x: mlpreg.predict([[x]])[0]


#Optimizer that minimizes a given function with CMA-ES.
def FMin(f, x_init, x_min, x_max):
  options= {'bounds':[[x_min], [x_max]], 'verb_log':0,'popsize':4}
  res= cma.fmin(lambda x:f(x[0]), [x_init], 0.5, options)
  return res[0][0]


if __name__=='__main__':
  #Finger robot test:
  #dxl= SetupRobot()
  #MoveToInit(dxl)
  #MoveToTrg(dxl, 0.2, 1.0)
  #raw_input('Waiting a key: ')
  #MoveToTrg(dxl, 0.8, 0.7)

  #GPR test:
  data_x= [0.5, 0.6, 0.8, 1.0]
  data_y= [0.2, 0.4, 0.7, 0.8]
  #f= TrainGPR(data_x, data_y)
  f= TrainMLPR(data_x, data_y)

  #Now we can compute y=f(x) for any x
  print 'f(0.55)=',f(0.55)

  #Plot f and (data_x, data_y)
  plot= PlotF(f, xmin=0.0, xmax=1.0, show=False)
  plot.title('GPR')
  plot.xlabel('x')
  plot.ylabel('y')
  plot.plot(data_x, data_y, 'o')
  plot.show()
  raw_input('Waiting a key: ')

  #Optimization test:

  def f_error(x):
    y_trg= 0.6
    return (y_trg-f(x))**2

  x_des= FMin(f_error, 0.5, 0.0, 1.0)
  print 'Solution:', x_des, f_error(x_des), f(x_des)

  plot.plot([x_des], [[f(x_des)]], '*')
  plot.show()

  raw_input('Waiting a key: ')


