#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plot
import math

#Rotation matrix
def Rot(th):
  return np.array([[math.cos(th), -math.sin(th)],
                   [math.sin(th),  math.cos(th)]])

#Forward kinematics with given joint angles q=[th_0,th_1,th_2]
#Return positions of joint-0 (base), 1, 2, and end-effector as a 2x4 matrix
def FK(q):
  #Link length
  link_len= 1.0

  #Pose of joint-0 (base): x,y
  x0= np.array([[0.0],
                [0.0]])

  #Position of joint-1
  x1= x0 + np.dot(Rot(q[0]),np.array([[link_len],
                                      [0.0]]))

  #Position of joint-2
  x2= x1 + np.dot(Rot(q[0]+q[1]),np.array([[link_len],
                                           [0.0]]))

  #Position of end-effector
  x3= x2 + np.dot(Rot(q[0]+q[1]+q[2]),np.array([[link_len],
                                                [0.0]]))

  return np.concatenate((x0,x1,x2,x3), axis=1)

if __name__=='__main__':
  plot.axis([-0.1,3.1,-0.1,3.1])
  X= FK([0.0,0.0,0.0])
  print X
  plot.plot(X[0],X[1],marker='o')
  X= FK([0.78,0.78,0.78])
  print X
  plot.plot(X[0],X[1],marker='o')
  plot.show()

