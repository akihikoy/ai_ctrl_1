#!/usr/bin/python
#Download CMA-ES for Python from https://www.lri.fr/~hansen/cmaesintro.html
#and put cma.py in the same directory
import cma

def f(x):
  return (x[0]-2.0)**2 + (x[1]-3.0)**2

res= cma.fmin(f,[0.0,0.0],0.5,{'verb_log':0})
print res
print 'Result=',res[0]
