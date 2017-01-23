from scipy.optimize import linprog
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import cPickle

c = [-1., 0.]
x0_bounds = (0, 1./12.946)
x1_bounds = (0, 1./7.542)


P1 = np.linspace(0, 0.5, 50)
P2 = np.linspace(0, 0.5, 50)
X, Y, Z = [], [], []
Cd = 197.1
t = 0
cp1 = []
cp2 = []
for p1 in P1:
  for p2 in P2:
    A = [[p1, p2], [1., -1.]]
    b = [1./Cd, 0.]
    res = linprog(c, A_ub = A, b_ub = b, bounds = (x0_bounds, x1_bounds), \
         options = {"disp": True})
    # print res
    # print "p1 = %s, p2 = %s, C = %s, opt = %s" % (p1, p2, Cd, -res["fun"])
    X.append(p1)
    Y.append(p2)
    Z.append(-res["fun"])
    if -res["fun"] > t:
      t = max(t, -res["fun"])
    if -res["fun"] >= 1./12.947:
      cp1.append(p1)
      cp2.append(p2)

data = (X, Y, Z)
cPickle.dump(data, open("/Users/ywan/Documents/myGithub/MCM/data.pkl", "wb"))
print t, 1./t, cp1, cp2
# fig = plt.figure()
# ax = Axes3D(fig)
# X, Y = np.meshgrid(X, Y)
# ax.plot_surface(X, Y, Z)

#ax = plt.subplot(111, projection = '3d')
#ax.scatter(X, Y, Z)
#ax.set_zlabel('throughput')
#ax.set_ylabel('p3')
#ax.set_xlabel('p2')
## plt.show()
#plt.savefig('lp3d.png')
