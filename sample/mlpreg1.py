#!/usr/bin/python
#Multilayer perceptron for regression with scikit-learn.
#cf. http://scikit-learn.org/stable/modules/neural_networks_supervised.html

# Importing libraries...
import sys
sys.path.append('../sample')
from libplot import PlotF
import random, math
import numpy as np
from sklearn.neural_network import MLPRegressor

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

# Training MLP (Multilayer Perceptron for Regression) so that MLP can map from x to y.
mlpreg= MLPRegressor(activation='relu', hidden_layer_sizes=(20, 20), alpha=0.01, max_iter=2000)
mlpreg.fit(data_x, np.array(data_y).reshape(len(data_y)))
f= lambda x: mlpreg.predict([[x]])[0]

# Now we can compute y=f(x) for any x
print 'f(1.5)=',f(1.5)
print 'f(3.45)=',f(3.45)
print 'f(5.0)=',f(5.0)

# Generate data for plotting (copy and paste to Excel or Google Spreadsheet)
#for t in np.mgrid[-1.0:5.0:0.2]:
  #print t,f(t)

# Plot y=f(x) with GUI (uncomment):
plot= PlotF(f, xmin=-1.0, xmax=5.0, show=False)
plot.plot(data_x, data_y, 'o')
plot.show()

