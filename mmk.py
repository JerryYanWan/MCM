import math
import numpy as np
import pandas as pd
from datetime import datetime
import time
import argparse

if __name__ == '__main__':

  parser = argparse.ArgumentParser(
    description = "calculate the average" + \
      "queue length and wait time")
  parser.add_argument('-k',
                      default = 1,
                      type = int,
                      help = 'number of agents')
  parser.add_argument('--lamb',
                      default = 1.,
                      type = float,
                      help = 'lambda in M/M/k model')
  parser.add_argument('--mu',
                      default = 1.,
                      type = float,
                      help = 'mu in M/M/k model')
  args = parser.parse_args()

  
  lambda1 = 1.0/float(args.lamb)
  mu1 = 1.0/float(args.mu)
  k = args.k

  rho = lambda1/mu1
  sum1 = np.sum([math.pow(rho, i)/math.factorial(i) \
         for i in np.arange(0, k-1)])
  P0 = 1.0 / 
      ((k/(k-rho))*(math.pow(rho, k)/ math.factorial(k)) + sum1)
  
  L = P0 * 
    (np.sum([math.pow(rho, i)*i/math.factorial(i) \
      for i in np.arange(0, k-1)]) +
    math.pow(rho, k+1)/(math.factorial(k-1) *math.pow(k-rho, 2)) +
    math.pow(rho, k)*k/(math.factorial(k-1)*(k-rho)))

  print "P0 = %s, L = %s, W = %s" % (P0, L, L/lambda1)
