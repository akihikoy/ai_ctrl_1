#!/usr/bin/python
#Download CMA-ES for Python from https://www.lri.fr/~hansen/cmaesintro.html
#and put cma.py in the same directory

# Importing libraries...
from __future__ import print_function
import cma

# Objective function to be minimized
def f(x):
  return (x[0]-2.0)**2 + (x[1]-3.0)**2

# Run CMA-ES to minimize the function f
res= cma.fmin(f,[0.0,0.0],0.5,{'verb_log':0,'popsize':4})
# Parameters: cma.fmin(OBJ_FUNC, X_INIT, STD_DEV, OPTIONS)

print(res)
print('Result=',res[0])
