#!/usr/bin/python
from libspline import *
import matplotlib.pyplot as plot
import numpy as np
import random

key_points= [[random.random()*3.0,random.random()*2.0-1.0] for i in range(5)]
key_points.sort()
plot.plot([p[0] for p in key_points], [p[1] for p in key_points], 'o')

spline= TCubicHermiteSpline()
spline.Initialize(key_points, tan_method=spline.CARDINAL, c=0.0)

X= []
Y= []
for t in np.arange(key_points[0][0], key_points[-1][0], 0.001):
  x= spline.Evaluate(t)
  X.append(t)
  Y.append(x)

plot.plot(X,Y)
plot.show()
