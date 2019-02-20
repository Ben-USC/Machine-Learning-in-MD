import numpy as np
import random
from load_file import *

np.random.seed(16807)

## define operations in hidden layers:
def hiddenLayer(xin, w, b):
   global unary, binary
   z = np.dot(w, xin) + b
   yl = nonlinear(z)

## compute psi(x)
def psi(x):
   global NL ## number of layers
   global theta_w, theta_b ## free parameters
   yl = hiddenLayer( x, theta_w[0], theta_b[0] )
   for l in range(1,NL-1):
      yl = hiddenLayer( yl, theta_w[0], theta_b[0] )
   yl = np.dot(theta_w[l], theta_b[l])


kin, kout = 6, 5 ## input & output dimensions in each layer
nout = 4 #dimension of final output

## initialize free parameters w and b
theta_w = [] ## theta for w's
theta_b = [] ## theta for b's
theta_w.append( np.random.normal(0, 0.1, (kin, N)) )
theta_b.append( np.zeros(kin) )
for i in range(1,NL-1):
   theta_w.append( np.random.normal(0, 0.1, (kin, kout)) )
   theta_b.append( np.zeros(kin) )
theta_w.append( np.random.normal(0, 0.1, (nout, kout)) )
theta_b.append( np.zeros(nout) )

## test:
for it in theta_w:
   print(it)
for it in theta_b:
   print(it)
