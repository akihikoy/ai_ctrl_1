#!/usr/bin/python

# Importing libraries...
from __future__ import print_function
import math
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

# Objective function to be minimized
def f(x):
  #return (x[0]-2.0)**2 + (x[1]-3.0)**2
  return math.sin(0.5*x[0]**2-0.25*x[1]*x[1]) * math.cos(2.0*x[0]+1.0-math.exp(x[1]))

cols= ['g','r','c','m','y','k','w']
ci= 0
def callback(x):
  global ci
  #plot.plot(x[0],x[1],'x')
  plot3d.scatter(x[0],x[1],f(x),c=cols[ci%len(cols)],marker='x')
  ci+= 1

#Plot f(x)
XY= np.mgrid[-2:2:0.1,-2:2:0.1]
Z= np.vectorize(lambda x,y:f([x,y]))(XY[0],XY[1])
fig= plot.figure()
plot3d= Axes3D(fig)
plot3d.plot_wireframe(XY[0],XY[1],Z)
#plot3d.plot_surface(XY[0],XY[1],Z)

res= minimize(f,[0.01,0.01],callback=callback)
print(res)
print('Result=',res.x)
#plot.plot(res.x[0],res.x[1],'o')
plot3d.scatter(res.x[0],res.x[1],f(res.x),marker='o')
plot.show()
