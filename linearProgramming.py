from scipy.optimize import linprog
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import cPickle
import sys

c = [-1., 0.]
x0_bounds = (0, 1./12.946)
x1_bounds = (0, 1./7.542)


P1 = np.linspace(0, 0.5, 50)
P2 = np.linspace(0, 0.5, 50)
X, Y, Z = [], [], []
Cd = 197.1
for p1 in P1:
  for p2 in P2:
    A = [[p1, p2], [1., -1.]]
    b = [1./Cd, 0.]
    res = linprog(c, A_ub = A, b_ub = b, \
         bounds = (x0_bounds, x1_bounds), \
         options = {"disp": True})
    X.append(p1)
    Y.append(p2)
    Z.append(-res["fun"])

data = (X, Y, Z)
cPickle.dump(data, open(sys.argv[1], "wb"))
