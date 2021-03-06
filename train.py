import numpy as np
import random
from initialize import *

## define operations in hidden layers:
def hiddenLayer(x, w, b):
   global unary, binary
   z = np.dot(w, x) + b[:,None]
   yl = nonlinear(z)

## compute psi(x)
def psi(x):
   global NL ## number of layers
   global theta_w, theta_b ## free parameters
   yl = hiddenLayer( x, theta_w[0], theta_b[0] ) ## first layer
   for l in range(1,NL-1):
      yl = hiddenLayer( yl, theta_w[l], theta_b[l] ) ## middle layers
   yl = np.dot(theta_w[l], yl) + b[:,None] ## last layer

## compute gradient:
L_b = psi(Xtrain) - 

## test:
for it in theta_w:
   print(it)
for it in theta_b:
   print(it)
