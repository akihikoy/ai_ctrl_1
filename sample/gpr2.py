#!/usr/bin/python
#NOTE: Remove and Upgrade scikit-learn (v.1.8 is necessary)
#  sudo apt-get remove python-sklearn python-sklearn-lib
#  sudo pip install -U scikit-learn

# Importing libraries...
from __future__ import print_function
import sys
sys.path.append('../sample')
from libplot import PlotF
import random, math
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Generate data. data_x[i] and data_y[i] are paired.
data_x= [
  [-1.7, -1.5],
  [ 0.8, -0.1],
  [-1.9,  0.2],
  [ 1.4,  0.4],
  [-1.5,  0.4],
  [ 1.7,  1.1],
  [ 0.7,  0.7],
  [ 1.2, -1.2],
  [ 0.0,  0.5],
  [ 1.8,  1.5]]
data_y= [
  [-1.8],
  [-0.2],
  [-1.4],
  [ 1.4],
  [-1.5],
  [-0.5],
  [ 0.6],
  [ 0.8],
  [ 0.1],
  [-1.8]]


# Training GPR (Gaussian Process for Regression) so that GPR can map from x to y.
# You can play with different kernels
#kernel= C(1.0, (1e-3, 1e3)) * RBF(1.0, (0.1, 10.0))
#kernel= C(1.0, (1.0, 1.0)) * RBF(1.0, (0.1, 10.0))
#kernel= C(1.0, (1e-3, 1e3)) * RBF(3.0, (3.0, 3.0))
#kernel= RBF(1.0, (0.1, 10.0))
kernel= RBF(3.0, (3.0, 3.0))
gp= GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
gp.fit(data_x, data_y)
f= lambda x: gp.predict([x])[0,0]

# Now we can compute y=f(x) for any x
print('f([0.0,0.0])=',f([0.0,0.0]))
print('f([1.0,1.0])=',f([1.0,1.0]))
print('f([1.5,2.0])=',f([1.5,2.0]))

#Plot gp.predict(x)
plot,plot3d= PlotF(f, xmin=[-2,-2], xmax=[2,2], dx=0.1, show=False)
#Plot data points
plot3d.scatter(np.array(data_x).T[0],np.array(data_x).T[1],data_y,marker='*',color='red')
plot.show()

