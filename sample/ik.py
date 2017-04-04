#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plot
from fk import FK
from scipy.optimize import minimize

#Error function of inverse kinematics
def Error(q, x_trg):
  X= FK(q)
  return (X[0,3]-x_trg[0,0])**2 + (X[1,3]-x_trg[1,0])**2

#Inverse kinematics
def IK(x_trg, q0):
  res= minimize(lambda q: Error(q, x_trg), q0)
  #res= minimize(lambda q: Error(q, x_trg), q0, callback=Viz)
  #print res
  return res.x

#Visualization
def Viz(q):
  X= FK(q)
  #print X
  plot.plot(X[0],X[1],marker='o')

if __name__=='__main__':
  plot.axis([-0.1,3.1,-0.1,3.1])

  q0= [0.01,0.01,0.01,0.01]
  Viz(q0)

  q= IK(np.array([[1.5],
                  [0.0]]), q0)
  print q
  Viz(q)

  q= IK(np.array([[1.0],
                  [1.0]]), q0)
  print q
  Viz(q)

  plot.show()
