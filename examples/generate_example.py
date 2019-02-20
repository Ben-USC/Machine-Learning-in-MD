import math
import numpy as np
import random

np.random.seed(16807)

N = 1000

f1 = open("./example_data_1.txt","w")
f2 = open("./example_data_2.txt","w")

gf = 1.0/9.81

for i in range(N):
   x = random.uniform(-2.0,2.0)
   f1.write(f"{x} {gf*x}\n")
   f2.write(f"{x} {-math.sin(x)}\n")
f1.close()
f2.close()
