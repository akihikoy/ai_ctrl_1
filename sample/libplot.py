#!/usr/bin/python
#\file    libplot.py
#\brief   Simple plot interface
#\author  Akihiko Yamaguchi, info@akihikoy.net
#\version 0.1
#\date    Apr.04, 2017
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

# Plot y=f(x) in range[xmin,xmax]. Dimensionality of x can be 1 or 2.
# dx: Step size.
# show: do we show the plot?
# Return plot object (see below return statements).
def PlotF(f,xmin,xmax,dx=0.01,show=True):
  if not isinstance(xmin,(list,np.ndarray)):  xmin= [xmin]
  if not isinstance(xmax,(list,np.ndarray)):  xmax= [xmax]
  assert(len(xmin)==len(xmax))
  if len(xmin)==1:
    X= np.arange(xmin[0], xmax[0], dx)
    Y= [f(x) for x in X]
    plot.plot(X,Y)
    if show: plot.show()
    return plot
  elif len(xmin)==2:
    XY= np.mgrid[xmin[0]:xmax[0]:dx, xmin[1]:xmax[1]:dx]
    Z= np.vectorize(lambda x,y:f([x,y]))(XY[0],XY[1])
    fig= plot.figure()
    plot3d= Axes3D(fig)
    plot3d.plot_wireframe(XY[0],XY[1],Z)
    #plot3d.plot_surface(XY[0],XY[1],Z)
    if show: plot.show()
    return plot, plot3d
  else:
    raise Exception('PlotF does not work with f(x) where dim(x)>2')
