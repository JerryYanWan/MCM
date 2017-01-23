import xlrd
import sys
import numpy as np
import pandas as pd
from datetime import datetime
import time
import argparse

if __name__ == '__main__':

  parser = argparse.ArgumentParser(
    description = \
    "calculate the mean and variance from excel data")
  parser.add_argument('--excel',
                      help = 'load the excel file')
  parser.add_argument('--diff',
                      default = 0,
                      type = int,
                      help =
      'whether to calculate the time stamp or time,' + \
      ' 0(time stamp) | 1(time)')
  parser.add_argument('--col',
                      default = 0,
                      type = int,
                      help = 'columns to process')
  args = parser.parse_args()
  df = pd.read_excel(args.excel)
  date = df[df.columns[args.col]].dropna()

  if args.diff == 0:
    dateSecond = []
    print "calculate column %s, %s, diff time stamp" \
      %(args.col, df.columns[args.col])
    for d in date:
      dateSecond.append(d.minute*60 + d.second+d.microsecond/1e6)
    dateSecond = np.array(dateSecond, dtype='float')
    c = np.diff(dateSecond)
    print "mean = %s, var = %s" % (c.mean(), c.var())
  else:
    dateSecond = []
    print "calculate column %s, %s, interval time" \
      %(args.col, df.columns[args.col])
    for d in date:
      if args.col == 7:
        dateSecond.append(d.hour*60. + d.minute + d.second/1e6)
      else:
        dateSecond.append(d.minute*60 + d.second+d.microsecond/1e6)
    dateSecond = np.array(dateSecond, dtype='float')
    print "mean = %s, var = %s" % (dateSecond.mean(), dateSecond.var())
