#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:47:39 2018

@author: Ben
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

dat1 = []
f = open("./example_data_1.txt", "r")
temp = f.readlines(); f.close()
for dat in temp:
    tmp = np.asfarray( dat.strip("\n").split(), float)
    dat1.append(tmp)
dat1 = np.asarray(dat1)


dat2 = []
f = open("./example_data_2.txt", "r")
temp = f.readlines(); f.close()
for dat in temp:
    tmp = np.asfarray( dat.strip("\n").split(), float)
    dat2.append(tmp)
dat2 = np.asarray(dat2)

fig=plt.figure(figsize=(8,6))
plt.rc('font',family='Arial')


plt.plot(dat1[:,0], dat1[:,1],"r-",linewidth=2.0)
plt.xlabel("x1", fontsize=20); plt.ylabel("y1", fontsize=20)

'''
plt.xlabel("x1",fontsize=25)
plt.xticks(np.arange(-2.0, 2.1, step=1.0))
minorlx = MultipleLocator(0.5)
plt.axes().xaxis.set_minor_locator(minorlx)
majorlx = MultipleLocator(1.0)
plt.axes().xaxis.set_major_locator(majorlx)
plt.axes().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.xlim(-2.5,2.5)

plt.ylabel("y1",fontsize=25)
#plt.ylim(-1.0,7.0)
plt.yticks(np.arange(-0.5, 0.5, step=0.25))
minorly = MultipleLocator(0.125)
plt.axes().yaxis.set_minor_locator(minorly)
majorly = MultipleLocator(0.25)
plt.axes().yaxis.set_major_locator(majorly)
#plt.axes().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.ylim(-0.5, 0.5)

plt.setp(plt.axes().spines.values(), linewidth=2.0)
plt.axes().tick_params(axis='both', which='major', direction='out', length=6, width=2.0, colors='k',labelsize=24)
plt.axes().tick_params(axis='both', which='minor', direction='out', length=4, width=2.0, colors='k')
plt.axes().tick_params(which='both',top=True, right=True, direction='in')
plt.axes().tick_params(axis='both', which='major', pad=10)
'''

plt.tight_layout()
fig.savefig("./example_1.png", dpi=400, transparent=True)

fig=plt.figure(figsize=(8,6))
plt.rc('font',family='Arial')

plt.plot(dat2[:,0], dat2[:,1],"b-",linewidth=2.0)
plt.xlabel("x2", fontsize=20); plt.ylabel("y2", fontsize=20)
plt.tight_layout()
fig.savefig("./example_2.png", dpi=400, transparent=True)
