## File: ds4ua-assignment-12-solns.py
## Topic: Assignment 12 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import numpy as np # Load NumPy as np
import matplotlib.pyplot as plt # Load matplotlib.pyplot to create histograms

## 1.

mu = 0.076 # Set the fixed rate of return
bal = 50000 # Set the initial balance
print('40\t50000.00') # Print the initial balance
for i in range(25): # Loop through birthdays 41 to 65
    bal = bal * np.exp(mu) # Update the balance
    print('%d\t%.2f' % (i+41, bal)) # Print the new balance

"""
# 1
40      50000.00
41      53948.13
42      58208.01
43      62804.27
44      67763.45
45      73114.23
46      78887.52
47      85116.68
48      91837.71
49      99089.45
50      106913.81
51      115356.00
52      124464.81
53      134292.87
54      144896.98
55      156338.42
56      168683.30
57      182002.97
58      196374.39
59      211880.62
60      228611.26
61      246662.99
62      266140.14
63      287155.25
64      309829.77
65      334294.72
"""

## 2.

arr = np.zeros(100000) # An array to hold the 100,000 values
sd = 0.167 # Set the standard deviation
ct = 0 # A variable to hold the number of successful balances
for i in range(100000): # Simulate 100,000 times
    bal = 50000 # Set the initial balance
    for j in range(25): # Loop through birthdays 41 to 65
        bal = bal * np.exp(np.random.normal(mu, sd)) # Update the balance
    arr[i] = np.round(bal, 2) # Put the final balance in the array, rounded
    if bal >= 300000:
        ct = ct + 1 # If the final balance is at least 300,000, add 1 to the counter
print('The mean is %f.' % arr.mean()) # Print the mean balance
print('The median is %f.' % np.median(arr)) # Print the median balance
arr = np.sort(arr) # Sort the array
print('The confidence interval is (%.2f, %.2f).' % (arr[2499], arr[97499]))
# Print the confidence interval
print('The proportion of successes is %f.' % (ct / 100000)) # Print the proportion
# of successes
plt.hist(arr, bins=80, range=[0, 3000000]) # Print a histogram

"""
# 2
The mean is 475080.993671.
The median is 334600.445000.
The confidence interval is (65150.09, 1702861.45).
The proportion of successes is 0.552080.
Histogram attached.
"""

## 3.

bal = 50000 # Set the initial balance
print('40\t50000.00') # Print the initial balance
for i in range(25): # Loop through birthdays 41 to 65
    bal = bal * np.exp(mu) + 3000 # Update the balance
    print('%d\t%.2f' % (i+41, bal)) # Print the new balance

"""
# 3
40      50000.00
41      56948.13
42      64444.90
43      72533.63
44      81261.08
45      90677.66
46      100837.80
47      111800.22
48      123628.25
49      136390.25
50      150159.98
51      165017.00
52      181047.16
53      198343.11
54      217004.80
55      237140.05
56      258865.24
57      282305.91
58      307597.51
59      334886.20
60      364329.68
61      396098.09
62      430375.01
63      467358.53
64      507262.36
65      550317.10
"""

## 4.

arr = np.zeros(100000) # An array to hold the 100,000 values
ct = 0 # A variable to hold the number of successful balances
for i in range(100000): # Simulate 100,000 times
    bal = 50000 # Set the initial balance
    for j in range(25): # Loop through birthdays 41 to 65
        bal = bal * np.exp(np.random.normal(mu, sd)) + 3000 # Update the balance
    arr[i] = np.round(bal, 2) # Put the final balance in the array, rounded
    if bal >= 300000:
        ct = ct + 1 # If the final balance is at least 300,000, add 1 to the counter
print('The mean is %f.' % arr.mean()) # Print the mean balance
print('The median is %f.' % np.median(arr)) # Print the median balance
arr = np.sort(arr) # Sort the array
print('The confidence interval is (%.2f, %.2f).' % (arr[2499], arr[97499]))
# Print the confidence interval
print('The proportion of successes is %f.' % (ct / 100000)) # Print the proportion
# of successes
plt.hist(arr, bins=80, range=[0, 4100000]) # Print a histogram

"""
# 4
The mean is 742606.781040.
The median is 560794.770000.
The confidence interval is (150012.42, 2426530.69).
The proportion of successes is 0.815130.
Histogram attached.
"""

## 5.

bal = 50000 # Set the initial balance
inc = 3000 # Set the initial increment
print('40\t50000.00') # Print the initial balance
for i in range(25): # Loop through birthdays 41 to 65
    bal = bal * np.exp(mu) + inc # Update the balance
    inc = inc * np.exp(0.03) # Update the increment
    print('%d\t%.2f' % (i+41, bal)) # Print the new balance

"""
# 5
40      50000.00
41      56948.13
42      64536.26
43      72817.72
44      81850.12
45      91695.71
46      102421.74
47      114100.87
48      126811.61
49      140638.73
50      155673.82
51      172015.80
52      189771.51
53      209056.35
54      229994.92
55      252721.79
56      277382.29
57      304133.33
58      333144.36
59      364598.32
60      398692.74
61      435640.90
62      475673.06
63      519037.80
64      566003.51
65      616859.91
"""

## 6.

arr = np.zeros(100000) # An array to hold the 100,000 values
ct = 0 # A variable to hold the number of successful balances
for i in range(100000): # Simulate 100,000 times
    bal = 50000 # Set the initial balance
    inc = 3000 # Set the initial increment
    for j in range(25): # Loop through birthdays 41 to 65
        bal = bal * np.exp(np.random.normal(mu, sd)) + inc # Update the balance
        inc = inc * np.exp(0.03) # Update the increment
    arr[i] = np.round(bal, 2) # Put the final balance in the array, rounded
    if bal >= 300000:
        ct = ct + 1 # If the final balance is at least 300,000, add 1 to the counter
print('The mean is %f.' % arr.mean()) # Print the mean balance
print('The median is %f.' % np.median(arr)) # Print the median balance
arr = np.sort(arr) # Sort the array
print('The confidence interval is (%.2f, %.2f).' % (arr[2499], arr[97499]))
# Print the confidence interval
print('The proportion of successes is %f.' % (ct / 100000)) # Print the proportion
# of successes
plt.hist(arr, bins=80, range=[0, 4500000]) # Print a histogram

"""
# 6
The mean is 818321.161060.
The median is 631038.805000.
The confidence interval is (185008.62, 2558368.84).
The proportion of successes is 0.874950.
Histogram attached.
"""

## 7.

bal = 50000 # Set the initial balance
inc = 3000 # Set the initial increment
dec = 25000 # Set the initial decrement
for i in range(25): # Loop through birthdays 41 to 65
    bal = bal * np.exp(mu) + inc # Update the balance
    inc = inc * np.exp(0.03) # Update the increment
print('65\t%.2f' % bal) # Print the 65th birthday balance
mu = 0.035 # Set the fixed rate of return
for j in range(35): # Loop through birthdays 66 to 100
    bal = bal * np.exp(mu) - dec # Update the balance
    print('%d\t%.2f' % (j+66, bal)) # Print the new balance

"""
# 7
65      616859.91
66      613832.28
67      610696.80
68      607449.64
69      604086.82
70      600604.22
71      596997.57
72      593262.45
73      589394.28
74      585388.34
75      581239.70
76      576943.29
77      572493.84
78      567885.90
79      563113.83
80      558171.78
81      553053.70
82      547753.31
83      542264.13
84      536579.42
85      530692.22
86      524595.32
87      518281.25
88      511742.28
89      504970.39
90      497957.29
91      490694.38
92      483172.78
93      475383.25
94      467316.26
95      458961.93
96      450310.02
97      441349.93
98      432070.69
99      422460.92
100     412508.86
"""

## 8.

arr = np.zeros(100000) # An array to hold the 100,000 values
ct = 0 # A variable to hold the number of positive balances
for i in range(100000): # Simulate 100,000 times
    bal = 50000 # Set the initial balance
    inc = 3000 # Set the initial increment
    mu = 0.076 # Set the mean
    sd = 0.167 # Set the standard deviation
    for j in range(25): # Loop through birthdays 41 to 65
        bal = bal * np.exp(np.random.normal(mu, sd)) + inc # Update the balance
        inc = inc * np.exp(0.03) # Update the increment
    mu = 0.035 # Set the new mean
    sd = 0.051 # Set the new standard deviation
    for k in range(35): # Loop through birthdays 66 to 100
        bal = bal * np.exp(np.random.normal(mu, sd)) - dec # Update the balance
    arr[i] = np.round(bal, 2) # Put the final balance in the array, rounded
    if bal >= 0:
        ct = ct + 1 # If the final balance is positive, add 1 to the counter
print('The mean is %f.' % arr.mean()) # Print the mean balance
print('The median is %f.' % np.median(arr)) # Print the median balance
arr = np.sort(arr) # Sort the array
print('The confidence interval is (%.2f, %.2f).' % (arr[2499], arr[97499]))
# Print the confidence interval
print('The proportion of successes is %f.' % (ct / 100000)) # Print the proportion
# of positive balances
plt.hist(arr, bins=80, range=[-1800000, 13000000]) # Print a histogram

"""
# 8
The mean is 1199369.067734.
The median is 454739.600000.
The confidence interval is (-1100547.82, 7952006.95).
The proportion of successes is 0.635540.
Histogram attached.
"""