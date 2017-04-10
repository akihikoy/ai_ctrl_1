#!/usr/bin/python
#NOTE: Remove and Upgrade scikit-learn (v.1.8 is necessary)
#  sudo apt-get remove python-sklearn python-sklearn-lib
#  sudo pip install -U scikit-learn

# Importing libraries...
import sys
sys.path.append('../sample')
from libplot import PlotF
import random, math
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Generate data. data_x[i] and data_y[i] are paired.
data_x= [
  [0.0],
  [1.0],
  [3.0],
  [4.0]]
data_y= [
  [0.0],
  [2.0],
  [1.0],
  [3.0]]

# Training GPR (Gaussian Process for Regression) so that GPR can map from x to y.
# You can play with different kernels.
##kernel= C(1.0, (1e-3, 1e3)) * RBF(1.0, (0.1, 10.0))
#kernel= C(1.0, (1.0, 1.0)) * RBF(1.0, (0.1, 10.0))
#kernel= C(1.0, (1e-3, 1e3)) * RBF(3.0, (3.0, 3.0))
#kernel= RBF(1.0, (0.1, 10.0))
kernel= RBF(3.0, (3.0, 3.0))
gp= GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
gp.fit(data_x, data_y)
f= lambda x: gp.predict([[x]])[0,0]

# Now we can compute y=f(x) for any x
print 'f(1.5)=',f(1.5)
print 'f(3.45)=',f(3.45)
print 'f(5.0)=',f(5.0)

# Generate data for plotting (copy and paste to Excel or Google Spreadsheet)
for t in np.mgrid[-1.0:5.0:0.2]:
  print t,f(t)

# Plot y=f(x) with GUI (uncomment):
#plot= PlotF(f, xmin=-1.0, xmax=5.0, show=False)
#plot.plot(data_x, data_y, 'o')
#plot.show()

