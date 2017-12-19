## File: ds4ua-assignment-5-solns.py
## Topic: Assignment 5 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import pandas as pd

food = pd.read_csv('fastfood2.csv', index_col=0) # Read in the fast food data as
# a DataFrame

## 1a.

lunch = food.loc[food['meal'] == 'Lunch'] # Get the meals that were for lunch
lunch_ct = len(lunch) # Count the meals that were for lunch
all_ct = len(food) # Count the total number of meals
lunch_prop = lunch_ct / all_ct # Calculate the proportion of meals that were for lunch
print('The proportion of meals that were for lunch is %f' % lunch_prop)

"""
# 1a
The proportion of meals that were for lunch is 0.516522
"""

## 1b.

week_gp = food['secs'].groupby(food['dayofweek']) # Group the time data by day of the week
week_gp.mean() # Calculate and print the mean amount of time for each day of the week

"""
# 1b
dayofweek
Fri     216.234941
Mon     216.774747
Thur    216.605129
Tues    215.742300
Wed     216.282449
Name: secs, dtype: float64
"""

## 1c.

# Function that returns a 95% confidence interval for the proportion of drink only
# orders for DataFrame x
def confint(x):
    drink = x.loc[x['drinkonly'] == 'Yes'] # Get the drink only orders
    drink_ct = len(drink) # Count the drink only orders
    meal_ct = len(x) # Count all of the orders in x
    p_hat = drink_ct / meal_ct # Get the proportion of drink only orders
    upper = p_hat + 1.96*((p_hat*(1-p_hat)/meal_ct)**0.5) # Calculate the upper bound
    # of the CI
    lower = p_hat - 1.96*((p_hat*(1-p_hat)/meal_ct)**0.5) # Calculate the lower bound
    # of the CI
    return "(" + str(lower) + ", " + str(upper) + ")" # Return the confidence interval
    # as a string

meals = food.groupby(food['meal']) # Group the data by meal type
meals.apply(confint) # Calculate and return the confidence interval for each of the
# three meal types

"""
# 1c
meal
Breakfast     (0.2211740665675427, 0.23613394334162327)
Dinner        (0.12730476118757109, 0.1342341232723899)
Lunch        (0.12675719458238568, 0.13254281893086697)
dtype: object
# There is definitely is strong difference for breakfast, with breakfast orders
# being much likelier to be drink only. Lunch and dinner orders have roughly the
# same chance of being drink only.
"""

## 1d.

cost_gp = food['cost'].groupby(food['meal']) # Group the cost data by meal type
cost_gp.mean() # Calculate and print the mean cost for each meal type

"""
# 1d
meal
Breakfast    292.079191
Dinner       502.017676
Lunch        372.363622
Name: cost, dtype: float64
"""

## 1e.

# Function that returns the proportion of breakfast orders for a DataFrame x
def breakfast(x):
    bf = x.loc[x['meal'] == 'Breakfast'] # Get the breakfast orders
    bf_ct = len(bf) # Count the breakfast orders
    day_ct = len(x) # Count the total number of orders in x
    prop = bf_ct / day_ct # Get the proportion of breakfast orders
    return "The prop. of breakfast orders is " + str(prop) # Return the proportion
    # as a string

# Function that returns the proportion of lunch orders for a DataFrame x
def lunch(x):
    lun = x.loc[x['meal'] == 'Lunch'] # Get the lunch orders
    lun_ct = len(lun) # Count the lunch orders
    day_ct = len(x) # Count the total number of orders in x
    prop = lun_ct / day_ct # Get the proportion of lunch orders
    return "The prop. of lunch orders is " + str(prop) # Return the proportion as
    # a string

# Function that returns the proportion of dinner orders for a DataFrame x
def dinner(x):
    din = x.loc[x['meal'] == 'Dinner'] # Get the dinner orders
    din_ct = len(din) # Count the dinner orders
    day_ct = len(x) # Count the total number of orders in x
    prop = din_ct / day_ct # Get the proportion of dinner orders
    return "The prop. of dinner orders is " + str(prop) # Return the proportion as
    # a string

mealprop_gp = food.groupby(food['dayofweek']) # Group the data by day of the week
mealprop_gp.apply(breakfast) # Calculate and print the proportion of breakfast orders
# for each day of the week
mealprop_gp.apply(lunch) # Calculate and print the proportion of lunch orders for each
# day of the week
mealprop_gp.apply(dinner) # Calculate and print the proportion of dinner orders for
# each day of the week

"""
# 1e
dayofweek
Fri     The prop. of breakfast orders is 0.12141828474...
Mon     The prop. of breakfast orders is 0.12016464987...
Thur    The prop. of breakfast orders is 0.12245411113...
Tues    The prop. of breakfast orders is 0.11983757551...
Wed     The prop. of breakfast orders is 0.11990154711...
dtype: object

dayofweek
Fri     The prop. of lunch orders is 0.5200377414709242
Mon     The prop. of lunch orders is 0.5155723070819281
Thur    The prop. of lunch orders is 0.5160673874779985
Tues     The prop. of lunch orders is 0.516440526889175
Wed     The prop. of lunch orders is 0.5144665461121157
dtype: object

dayofweek
Fri     The prop. of dinner orders is 0.35854397377960967
Mon     The prop. of dinner orders is 0.36426304304701446
Thur    The prop. of dinner orders is 0.36147850138295196
Tues    The prop. of dinner orders is 0.36372189759334456
Wed     The prop. of dinner orders is 0.36563190677114726
dtype: object
"""

## 1f.

avetime_means = food['secs'].groupby(food.index).mean() # Get the average fill time
# for each of the 892 stores
mean_all = avetime_means.mean() # Get the mean of the averages of all the stores
std_all = avetime_means.std(ddof=1) # Get the sample standard deviation of the averages
upper_bound = mean_all + 2*std_all # Get the low-performing cutoff point
lower_bound = mean_all - 2*std_all # Get the high-performing cutoff point
print('The high-performing stores are:')
avetime_means.loc[avetime_means.values <= lower_bound] # Find and print all of the
# high-performing stores
print('The low-performing stores are:')
avetime_means.loc[avetime_means.values >= upper_bound] # Find and print all of the
# low-performing stores

"""
# 1f
The high-performing stores are:
storenum
27     184.487179
43     188.419643
53     188.631148
122    180.400000
201    185.615385
243    173.637931
312    187.411765
500    187.403509
511    175.470000
514    184.151786
550    180.363636
570    183.800000
651    186.946429
699    186.082192
722    188.973451
852    189.460674
859    187.463158
Name: secs, dtype: float64

The low-performing stores are:
storenum
30     247.413534
47     245.446809
59     244.228571
128    247.854167
149    254.926316
154    247.103774
155    244.339130
231    255.208696
233    245.375000
281    249.500000
318    245.991453
387    248.477064
392    245.058252
402    246.212598
422    254.519231
452    243.153846
474    243.724771
528    250.406250
614    243.913793
621    250.213592
657    264.463918
718    248.175000
723    248.692308
725    245.333333
726    244.935780
887    250.571429
Name: secs, dtype: float64
"""

## 1g.

avetime_med = food['secs'].groupby(food.index).median() # Get the median fill time
# for each of the 892 stores
med_all = avetime_med.mean() # Get the mean of the medians of all the stores
std_med = avetime_med.std(ddof=1) # Get the sample standard deviation of all the medians
upper_bd = med_all + 2*std_med # Get the low-performing cutoff point
lower_bd = med_all - 2*std_med # Get the high-perofrming cutoff point
high_perf = avetime_med.loc[avetime_med.values <= lower_bd] # Get the high-performing
# stores according to the medians
low_perf = avetime_med.loc[avetime_med.values >= upper_bd] # Get the low-performing
# stores accordinfg to the medians
high = [] # Create a list to hold the high-performing stores in both methods
# Loop through the high-performing stores from both methods, if they match and are
# thus in both lists, add those stores to the combined list
for x in high_perf.index:
    for y in avetime_means.loc[avetime_means.values <= lower_bound].index:
        if x == y:
            high.append(y)
low = [] # Create a list to hold the low-performing stores in both methods
# Loop through the low-performing stores from both methods, if they match and are
# thus in both lists, add those stores to the combined list
for x in low_perf.index:
    for y in avetime_means.loc[avetime_means.values >= upper_bound].index:
        if x == y:
            low.append(y)
print('The stores in both high-performing groups are:')
print(list(high)) # Print the list of high-performing stores in both methods
print('The stores in both low-performing groups are:')
print(list(low)) # Print the list of low-performing stores in both methods

"""
# 1g
The stores in both high-performing groups are:
[27, 243, 312, 722]
The stores in both low-performing groups are:
[59, 149, 233, 318, 402, 452, 528, 657, 718, 723, 725, 726, 887]
"""

food2 = pd.read_csv('fastfood3.csv', index_col=0) # Read in the fast food data as
# a DataFrame

## 2a.

highest = food2.loc[food2['satisfaction'] == 10] # Get the orders with the highest
# possible rating
highest_ct = len(highest) # Count the customers that gave the highest possible rating
lowest = food2.loc[food2['satisfaction'] == 1] # Get the orders with the lowest
# possible rating
lowest_ct = len(lowest) # Count the customers that gave the lowest possible rating
all_ct = len(food2) # Count the total number of customers
highest_perc = 100 * (highest_ct/all_ct) # Get the percentage of customers that
# gave the highest possible rating
lowest_perc = 100 * (lowest_ct/all_ct) # Get the percentage of customers that gave
# the lowest possible rating
print('%f percent of customers gave the highest possible satisfaction rating.' % highest_perc)
print('%f percent of customers gave the lowest possible satisfaction rating.' % lowest_perc) 

"""
# 2a
0.129627 percent of customers gave the highest possible satisfaction rating.
0.004986 percent of customers gave the lowest possible satisfaction rating.
"""

## 2b.

satis_gp = food2['satisfaction'].groupby(food2['dayofweek']) # Group the satisfaction
# ratings by day of the week
satis_gp.mean() # Calculate and print the mean satisfaction for each day of the week

"""
# 2b
dayofweek
Fri     6.116154
Mon     6.132017
Thur    6.118582
Tues    6.142121
Wed     6.141752
Name: satisfaction, dtype: float64
"""

## 2c.

# Function that returns a 95% confidence interval for the proportion of satisfied
# customers for a DataFrame x
def conf(x):
    satis = x.loc[x['satisfaction'] >= 7] # Get the satisfied customers
    satis_ct = len(satis) # Count the satisfied customers
    meal_ct = len(x) # Count the total number of customers
    p_hat = satis_ct / meal_ct # Calculate the proportion of satisifed customers
    upper = p_hat + 1.96*((p_hat*(1-p_hat)/meal_ct)**0.5) # Get the upper bound for
    # the CI
    lower = p_hat - 1.96*((p_hat*(1-p_hat)/meal_ct)**0.5) # Get the lower bound for
    # the CI
    return "(" + str(lower) + ", " + str(upper) + ")" # Return the CI as a string

satisfied_gp = food2.groupby(food2['meal']) # Group the data by meal type
satisfied_gp.apply(conf) # Find and print the confidence interval for each meal type

"""
# 2c
meal
Breakfast     (0.5439933589067114, 0.5617044115309435)
Dinner         (0.4330352502477782, 0.443232721272688)
Lunch        (0.35876723189754983, 0.3670488720386676)
dtype: object
"""

## 2d.

quick_satis = food2.loc[(food2['secs'] <= 180) & (food2['satisfaction'] >= 7)]
# Get the orders that took no more than 180 seconds and satified their customers
quick_satis_ct = len(quick_satis) # Count these orders
quick = food2.loc[food2['secs'] <= 180] # Get the orders that took no more than 180
# seconds
quick_ct = len(quick) # Count the orders that took no more than 180 seconds
p_hat = quick_satis_ct / quick_ct # Get the proportion of satisfied customers among
# orders that took no more than 180 seconds
upper = p_hat + 1.96*((p_hat*(1-p_hat)/quick_ct)**0.5) # Get the upper bound of the CI
lower = p_hat - 1.96*((p_hat*(1-p_hat)/quick_ct)**0.5) # Get the lower bound of the CI
long_satis = food2.loc[(food2['secs'] >= 360) & (food2['satisfaction'] >= 7)]
# Get the orders that took at least 360 seconds and satified their customers
long_satis_ct = len(long_satis) # Count these orders
long = food2.loc[food2['secs'] >= 360] # Get the orders that took at least 360 seconds
long_ct = len(long) # Count the orders that took at least 360 seconds
p_hat2 = long_satis_ct / long_ct # Get the proportion of satisfied customers among
# orders that took at least 360 seconds
upper2 = p_hat2 + 1.96*((p_hat2*(1-p_hat2)/long_ct)**0.5) # Get the upper bound of
# the CI
lower2 = p_hat2 - 1.96*((p_hat2*(1-p_hat2)/long_ct)**0.5) # Get the lower bound of
# the CI
print('The CI for quick orders is (%f, %f).' % (lower, upper))
print('The CI for long orders is (%f, %f).' % (lower2, upper2))

"""
# 2d
The CI for quick orders is (0.532175, 0.540387).
The CI for long orders is (0.102436, 0.111396).
"""

## 2e.

# Function that returns 1 if the order is breakfast, and 0 otherwise
def bf(x):
    if x == 'Breakfast':
        return(1)
    else:
        return(0)
    
bf_ind = food2['meal'].apply(bf) # Get a series of 1s and 0s corresponding to orders
# that were breakfast or not, respectively
food2['predsatis'] = 4 + 0.002*food2['cost'] - 0.005*food2['secs'] + bf_ind
# Create a column called 'predsatis', and fill it with the result of the formula
# for each order
mean_pred = food2['predsatis'].mean() # Calculate the mean predicted satisfaction rating
print('The mean predicted rating is %f.' % mean_pred)

"""
# 2e
The mean predicted rating is 3.858513.
"""

## 2f.

diff = food2['satisfaction'] - food2['predsatis'] # Find the difference between
# the actual satisfaction rating and the predicted rating
diff = diff.abs() # Get the absolute value of this difference
max_diff = diff.max() # Find the maximum difference
min_diff = diff.min() # Find the minimum difference
ave_diff = diff.mean() # Find the average difference
print('The maximum difference is %f.' % max_diff)
print('The minimum difference is %f.' % min_diff)
print('The average difference is %f.' % ave_diff)

"""
# 2f
The maximum difference is 4.896000.
The minimum difference is 0.000000.
The average difference is 2.272899.
"""