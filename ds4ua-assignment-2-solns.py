## File: ds4ua-assignment-2-solns.py
## Topic: Assignment 2 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


#### Assignment 2, Part A

import numpy as np

## A1.

x = np.random.uniform(low=0, high=20, size=10000)
ct = 0
for i in x:
    if i >= 5 and i <= 12:
        ct += 1
percent = ct / 100 # (ct / 10000) * 100
print('%.2f percent of the values are in the interval [5,12].' % percent)

"""
# A1
34.97 percent of the values are in the interval [5,12].
"""

## A2.

ctarray = np.zeros(500)
for i in range(500):
    ct = 0
    x2 = np.random.uniform(low=0, high=20, size=10000)
    for e in x2:
        if e >= 5 and e <= 12:
            ct += 1
        ctarray[i] = ct / 100 # (ct / 10000) * 100
result = np.mean(ctarray)
print('The average of the 500 percentages is %f.' % result)

"""
# A2
The average of the 500 percentages is 35.004860.
"""

## A3.

ct = 1
choice = np.random.choice(x, size=1)
while choice >= 4:
    ct += 1
    choice = np.random.choice(x, size=1)
print('The number of random entires required is %d.' % ct)

"""
# A3
The number of random entires required is 2.
"""

## A4.

ctarray = np.zeros(1000)
for i in range(1000):
    ct = 1
    choice = np.random.choice(x, size=1)
    while choice >= 4:
        ct += 1
        choice = np.random.choice(x, size=1)
    ctarray[i] = ct
result = np.mean(ctarray)
print('The average for the number of entires required is %f.' % result)

"""
# A4
The average for the number of entires required is 5.123000.
"""

## A5.

ct = 1
t = 1
choice = np.random.choice(x, size=1)
while choice <= 12 or t < 3:
    ct += 1
    if choice > 12:
        t += 1
    choice = np.random.choice(x, size=1)
print('The number of random entries required is %d.' % ct)

"""
# A5
The number of random entries required is 4.
"""

## A6.

ctarray = np.zeros(1000)
for i in range(1000):
    ct = 1
    t = 1
    choice = np.random.choice(x, size=1)
    while choice <= 12 or t < 3:
        ct += 1
        if choice > 12:
            t += 1
        choice = np.random.choice(x, size=1)
    ctarray[i] = ct
result = np.mean(ctarray)
print('The average for the number of entries required is %f.' % result)

"""
# A6
The average for the number of entries required is 7.570000.
"""

#%%

#### Assignment 2, Part B

import numpy as np 
p1 = np.random.normal(40,12,size=500000)
    
## B.a.i
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=10)
    xbar = np.mean(s)
    left = xbar - 1.96 * 12 / (10**0.5)
    right = xbar + 1.96 * 12 / (10**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.a.i
The proportion of confidence intervals that contain the population mean is 0.9532.
"""

## B.a.ii
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=20)
    xbar = np.mean(s)
    left = xbar - 1.96 * 12 / (20**0.5)
    right = xbar + 1.96 * 12 / (20**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.a.ii
The proportion of confidence intervals that contain the population mean is 0.9496.
"""

## B.a.iii

ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=30)
    xbar = np.mean(s)
    left = xbar - 1.96 * 12 / (30**0.5)
    right = xbar + 1.96 * 12 / (30**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.a.iii
The proportion of confidence intervals that contain the population mean is 0.9472.
"""

## B.b.i
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=10)
    xbar = np.mean(s)
    stdev = np.std(s, ddof=1)
    left = xbar - 1.96 * stdev / (10**0.5)
    right = xbar + 1.96 * stdev / (10**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.b.i
The proportion of confidence intervals that contain the population mean is 0.9189.
"""

## B.b.ii
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=20)
    xbar = np.mean(s)
    stdev = np.std(s, ddof=1)
    left = xbar - 1.96 * stdev / (20**0.5)
    right = xbar + 1.96 * stdev / (20**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.b.ii
The proportion of confidence intervals that contain the population mean is 0.9346.
"""

## B.b.iii
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=30)
    xbar = np.mean(s)
    stdev = np.std(s, ddof=1)
    left = xbar - 1.96 * stdev / (30**0.5)
    right = xbar + 1.96 * stdev / (30**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.b.iii
The proportion of confidence intervals that contain the population mean is 0.9366.
"""

## B.c.i

ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=10)
    xbar = np.mean(s)
    stdev = np.std(s, ddof=1)
    left = xbar - 2.262 * stdev / (10**0.5)
    right = xbar + 2.262 * stdev / (10**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.c.i
The proportion of confidence intervals that contain the population mean is 0.9516.
"""

## B.c.ii
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=20)
    xbar = np.mean(s)
    stdev = np.std(s, ddof=1)
    left = xbar - 2.093 * stdev / (20**0.5)
    right = xbar + 2.093 * stdev / (20**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.c.ii
The proportion of confidence intervals that contain the population mean is 0.9519.
"""

## B.c.iii
    
ct = 0
for i in range(10000):
    s = np.random.choice(p1, size=30)
    xbar = np.mean(s)
    stdev = np.std(s, ddof=1)
    left = xbar - 2.045 * stdev / (30**0.5)
    right = xbar + 2.045 * stdev / (30**0.5)
    if left <= 40 and 40 <= right:
        ct += 1
prop = ct / 10000
print('The proportion of confidence intervals that contain the population mean is %.4f.' % prop)

"""
# B.c.iii
The proportion of confidence intervals that contain the population mean is 0.9495.
"""
