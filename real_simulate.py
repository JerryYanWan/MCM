import numpy as np
from numpy import random as rm
import pandas as pd
import xlrd
import sys
from datetime import datetime
import time

df = pd.read_excel(sys.argv[1])
print df.dtypes
date1 = df['TSA Pre-Check Arrival Times'].dropna() #= pd.to_datetime(df['TSA Pre-Check Arrival Times'])
date2 = df['Regular Pax Arrival Times'].dropna()
date3 = df['ID Check Process Time 1'].dropna()
date4 = df['ID Check Process Time 2'].dropna()
date = date2
dateSecond = []
for d in date:
  print d
  dateSecond.append(d.minute*60 + d.second+d.microsecond/1e6)
dateSecond = np.array(dateSecond, dtype='float')
print dateSecond
process = 12.5514
def simulation(T = 600):

  t = 0; nA = 0; nD = 0; n = 0; A = []; D = []; N = []; S = []
  # tA = rm.exponential(10, 1)
  tD = np.inf

  index = 0
  tA = dateSecond[index]
  index += 1
  while True:
    if (tA <= tD and index < len(dateSecond)):
      t = tA
      nA = nA + 1
      n = n + 1
      tA = t + rm.exponential(10, 1)
      tA = dateSecond[index]
      index += 1
      if n == 1:
        # tS = rm.uniform(5, 10, 1)
        tS = process
        tD = t + tS
        S.append(tS)
      A.append(t)
    elif (tD <= tA):
      t = tD; n = n - 1
      nD = nD + 1
      if n == 0:
        tD = np.inf
      else:
        # tS = rm.uniform(5, 10, 1)
        tS = process
        tD = t + tS
        S.append(tS)
      D.append(t)
      N.append(n)
    elif (index >= len(dateSecond)):
      break

  while True:
    if n <= 0:
      break
    t = tD; n = n - 1;
    nD = nD + 1
    D.append(t)
    N.append(n)
    if n > 0:
      # tS = rm.uniform(5, 10, 1)
      tS = process
      tD = t + tS
      S.append(tS)
  Tp = max(t - T, 0)
  raw = {'A': A, 'D': D, 'S': S, 'N': N}
  data = pd.DataFrame(raw)
  print A
  print D
  print S
  print np.mean(N)
  return {'count': data.N.count(), 'wcount':sum(data.N > 0),
    'avgwait': float(np.mean(data.D - data.A - data.S))}

res = [simulation() for i in range(1)]
print res[0]['avgwait']
#res = pd.DataFrame(res)
#res
#
#import matplotlib.pyplot as plt
#plt.hist(res.avgwait)
#plt.show()
