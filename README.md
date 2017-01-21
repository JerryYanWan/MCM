# The simple scripts to calculate the mean and variance of data from excel in problem D.

## load.py
This script can load in the excel and calculate the mean and variance by giving the argument parameters.

```
optional arguments:
  -h, --help     show this help message and exit
  --excel EXCEL  load the excel file
  --diff DIFF    whether to calculate the time stamp or time, 0(time stamp) |
                 1(time)
  --col COL      columns to process
```

## calculate.py
This script will calculate the average queue length and wait time by the definition and deduction of M/M/k model.

```
optional arguments:
  -h, --help   show this help message and exit
  -k K         number of agents
  --lamb LAMB  lambda in M/M/k model
  --mu MU      mu in M/M/k model
```
