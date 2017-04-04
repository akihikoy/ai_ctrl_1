#!/usr/bin/python
from scipy.optimize import minimize

def f(x):
  return (x[0]-2.0)**2 + (x[1]-3.0)**2

res= minimize(f,[0.0,0.0])
print res
print 'Result=',res.x
