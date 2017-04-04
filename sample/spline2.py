#!/usr/bin/python
from libspline import *
from libplot import PlotF
import numpy as np
import random

# We randomly generate key points.
key_points= [[random.random()*3.0,random.random()*2.0-1.0] for i in range(5)]
key_points.sort()  # Need to sort by x
spline= TCubicHermiteSpline()
spline.Initialize(key_points, tan_method=spline.CARDINAL, c=0.0)
f= spline.Evaluate

# Now we can compute y=f(x) for any x

# Plot y=f(x):
plot= PlotF(f, xmin=key_points[0][0], xmax=key_points[-1][0], show=False)
plot.plot([p[0] for p in key_points], [p[1] for p in key_points], 'o')
plot.show()
