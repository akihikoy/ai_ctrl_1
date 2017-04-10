#!/usr/bin/python

# Importing libraries...
import sys
sys.path.append('../sample')
from libspline import *
from libplot import PlotF
import numpy as np
import random

# Define key points (pairs of [x,y]).
key_points= [
  [0.0, 0.0],
  [1.0, 2.0],
  [3.0, 1.0],
  [4.0, 3.0]]
spline= TCubicHermiteSpline()
spline.Initialize(key_points, tan_method=spline.CARDINAL, c=0.0)
f= spline.Evaluate

# Now we can compute y=f(x) for any x
print 'f(1.5)=',f(1.5)
print 'f(3.45)=',f(3.45)
print 'f(5.0)=',f(5.0)  # This does not work as it is an extrapolation

# Generate data for plotting (copy and paste to Excel or Google Spreadsheet)
for t in np.mgrid[0.0:4.0:0.1]:
  print t,f(t)

# Plot y=f(x) with GUI (uncomment):
#plot= PlotF(f, xmin=0.0, xmax=4.0, show=False)
#plot.plot([p[0] for p in key_points], [p[1] for p in key_points], 'o')
#plot.show()
