import numpy as np
import random

np.random.seed(16807)

## define sigmoid function
def sigmoid(x):
   return 1.0/(1.0+np.exp(-1.0*x))

## define unary and binary operations:
unary = [lambda x: x, np.sin, np.cos, sigmoid]
binary = lambda x1, x2: x1 * x2

## define nonlinear operations given z
def nonlinear(z): ## dim(z) is 6 in the example
   global unary, binary
   xout = []
   Nz = np.shape(z)[0]; Nu = 4; Nb = Nz - Nu
   #Nu = int(0.4*Nz) ## 40% of z goes to unary operations
   #if (Nz-Nu)%2 != 0: NU = NU-1; NB = Nz - NU
   #NB = Nz - NU
   for i in range(Nu):
      xout.append(unary[i%4](z))
   for i in range(Nu, Nz):
      xout.append(binary(z[i], z[i+1]))
      i += 1
   return xout

'''
## ------------ read data file ---------
f = open("./data.txt","r")
temp = f.readlines()[0:]
X = []
for dat in temp:
   tmp = np.asfarray(dat.strip("\n").split(), float)
   X.append(tmp)
X = np.asarray(X)
## ----------------------------------
'''
##read training set:
Xtrain = np.random.normal(0,0.1, (2, 10))
Ytrain = np.random.normal(0,0.1, 10)
D,N = np.shape(Xtrain)## size of training set

NL = 2 ## number of layers in the training set
kin, kout = 6, 5 ## input & output dimensions in each layer
nout = D #dimension of final output, equal to training set dimension in the example

## initialize free parameters w and b
theta_w = [] ## theta for w's
theta_b = [] ## theta for b's
theta_w.append( np.random.normal(0, 0.1, (kin, D)) ) ## random number for w's
theta_b.append( np.zeros(kin) ) ## 0 for all b's
for i in range(1,NL-1):
   theta_w.append( np.random.normal(0, 0.1, (kin, kout)) )
   theta_b.append( np.zeros(kin) )
theta_w.append( np.random.normal(0, 0.1, (nout, kout)) )
theta_b.append( np.zeros(nout) )

