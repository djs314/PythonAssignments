## File: ds4ua-assignment-4-solns.py
## Topic: Assignment 4 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import pandas as pd
import numpy as np

ff = pd.read_csv('fastfood1.csv', index_col=0) # Read in fast food data
ff = ff.iloc[:,0] # Convert data from Dataframe to series

## 1a.

time = ff.values # Store the time values in an array
ave_time = np.mean(time) # Calculate the mean of all values
print('The average time required to fill all orders is %f seconds.' % ave_time)

"""
# 1a
The average time required to fill all orders is 216.327108 seconds.
"""

## 1b.

max_time = 0 # Holds the maximum amount of time
for x in time:
    if x > max_time:
        max_time = x # For each value, if it it greater than the previous value,
                     # set as the new maximum
print('The maximum amount of time required to fill an order is %d seconds.' % max_time)

min_time = 10000 # Holds the minimum amount of time
for x in time:
    if x < min_time:
        min_time = x # For each value, if it is less than the previous value,
                     # set as the new minimum
print('The minimum amount of time required to fill an order is %d seconds.' % min_time)

max_list = ff.loc[ff.values == max_time].values # Store all the values with the max
# amount of time in an array
print('The number of orders with the maximum time is %d.' % len(max_list))
# Calculate the number of orders with the maximum time and print

min_list = ff.loc[ff.values == min_time].values # Store all the values with the min
# amount of time in an array
print('The number of orders with the minimum time is %d.' % len(min_list))
# Calculate the number of orders with the minimum time and print

"""
# 1b
The maximum amount of time required to fill an order is 600 seconds.
The minimum amount of time required to fill an order is 30 seconds.
The number of orders with the maximum time is 23.
The number of orders with the minimum time is 123.
"""

## 1c.

store777 = ff.loc[777].values # Get the time values for store 777
ave_time777 = np.mean(store777) # Calculate the mean of the values
print('The average time required by store 777 to fill its orders is %f seconds.' % ave_time777)

"""
# 1c
The average time required by store 777 to fill its orders is 198.519084 seconds.
"""

## 1d.

store321 = ff.loc[321] # Get the records from store 321
print('The number of records from store 321 is %d.' % len(store321))
# Calculate the number of records from store 321 and print

"""
# 1d
The number of records from store 321 is 97.
"""

## 1e.

ff_sorted = ff.sort_index() # Sort the series by store number
stores7 = ff_sorted.loc[700:750].values # Get the values of stores 700-750
ave_stores = np.mean(stores7) # Calculate the mean of the values
print('The mean amount of time to fill an order by stores 700-750 is %f seconds.' % ave_stores)

"""
# 1e
The mean amount of time to fill an order by stores 700-750 is 215.892454 seconds.
"""

## 1f.

stores5 = ff_sorted.loc[500:600] # Get the records for stores 500-600
n = len(stores5) # Get the number of records from stores 500-600

stores200 = stores5.loc[stores5.values > 200] # Get the records from stores 500-600
# that required more than 200 seconds to fill
n2 = len(stores200) # Get the number of records from stores 500-600 that required
# more than 200 seconds to fill

p_hat = n2/n # Get the proportion
upper = p_hat + 1.96*((p_hat*(1-p_hat)/n)**0.5) # Get the upper bound of the CI
lower = p_hat - 1.96*((p_hat*(1-p_hat)/n)**0.5) # Get the lower bound of the CI
print('The 95 percent confidence interval for the proportion is (%f, %f).' % (lower, upper))

"""
# 1f
The 95 percent confidence interval for the proportion is (0.368389, 0.386206).
"""

## 1g.

ff_index = ff_sorted.index # Get a list of the indicies
i_prev = ff_index[0] # Holds the previous store index, which will be compared to the
# current one
store_nums = [ff_index[0]] # Make a list to hold the distinct store indicies
for i in ff_index: # Loop through each store index, and when a distinct index is found,
    # add it to the list
    if i != i_prev:
        store_nums.append(i)
        i_prev = i
print('The number of distinct stores in the data set is %d.' % len(store_nums))
# Get the number of distinct stores and print

"""
# 1g
The number of distinct stores in the data set is 892.
"""

## 1h.

min_mean = 10000 # Holds the current minimum mean
min_store = 0 # Holds the store number associated with the current minimum mean
for i in store_nums: # Loop through all the stores
    store_i = ff.loc[i].values
    ave_time_i = np.mean(store_i) # Calculate the mean of each store
    if ave_time_i < min_mean: # If the current mean is lower than the minimum
    # mean, make it the new minimum mean, and get the associated store number
        min_mean = ave_time_i
        min_store = i
print('Store %d has the lowest mean order time.' % min_store)

max_mean = 0 # Holds the current maximum mean
max_store = 0 # Holds the store number associated with the current maximum mean
for i in store_nums: # Loop through all the stores
    store_i = ff.loc[i].values
    ave_time_i = np.mean(store_i) # Calculate the mean of each store
    if ave_time_i > max_mean: # If the current mean is higher than the maximum
    # mean, make it the new maximum mean, and get the associated store number
        max_mean = ave_time_i
        max_store = i
print('Store %d has the highest mean order time.' % max_store)

"""
# 1h
Store 243 has the lowest mean order time.
Store 657 has the highest mean order time.
"""

## 1i.

num_stores = [] # A list to hold the number of orders of each store
for i in store_nums:
    num_i = len(ff.loc[i]) # For each distinct store, get the number of orders
    num_stores.append(num_i) # Add the number of orders of each store to the list
med = np.median(num_stores) # Calculate the median
print('The median number of orders for a single store is %d.' % med)

"""
# 1i
The median number of orders for a single store is 112.
"""

grades = pd.read_csv('samplegrades.csv', index_col=0) # Read in grades data

## 2a.

course_ave = grades['CourseAve'] # Get the column of course averages
course_mean = np.mean(course_ave) # Calculate the mean
course_sd = np.std(course_ave, ddof=1) # Calculate the sample standard deviation
print('The mean for the Course Average is %f.' % course_mean)
print('The sample standard deviation for the Course Average is %f.' % course_sd)

sat_writing = grades['Write'] # Get the column of SAT writing scores
sat_writing_mean = np.mean(sat_writing) # Calculate the mean
sat_writing_sd = np.std(sat_writing, ddof=1) # Calculate the sample standard deviation
print('The mean for the SAT Writing score is %f.' % sat_writing_mean)
print('The sample standard deviation for the SAT Writing score is %f.' % sat_writing_sd)

"""
# 2a
The mean for the Course Average is 80.401150.
The sample standard deviation for the Course Average is 10.666467.
The mean for the SAT Writing score is 666.723404.
The sample standard deviation for the SAT Writing score is 94.455617.
"""

## 2b.

fem_final = grades.loc[grades['Gender'] == 'F', 'Final'] # Get the final exam scores
# for all females in the class
fem_final_mean = np.mean(fem_final) # Calculate the mean
print('The mean final exam score for all females in the class is %f.' % fem_final_mean)

"""
# 2b
The mean final exam score for all females in the class is 71.351792.
"""

## 2c.

male_final = grades.loc[(grades['Gender'] == 'M') & (grades['Sect'] == 'TR930'), 'Final']
# Get the final exam scores of all male students in the TR930 section
male_final_mean = np.mean(male_final) # Calculate the mean
print('The mean final exam score for all males in the TR930 section is %f.'
      % male_final_mean)

"""
# 2c
The mean final exam score for all males in the TR930 section is 68.153409.
"""

## 2d.

hw_1 = grades.loc[grades['Year'] == 1, 'HW'] # Get the homework scores for all 1st-years
hw_1_mean = np.mean(hw_1) # Calculate the mean
print('The mean homework score for all 1st-years is %f.' % hw_1_mean)

hw_4 = grades.loc[grades['Year'] == 4, 'HW'] # Get the homework scores for all 4th-years
hw_4_mean = np.mean(hw_4) # Calculate the mean
print('The mean homework score for all 4th-years is %f.' % hw_4_mean)

"""
# 2d
The mean homework score for all 1st-years is 189.243768.
The mean homework score for all 4th-years is 192.951724.
"""

## 2e.

second_yr = grades.loc[grades['Year'] == 2] # Get the 2nd-year students
second_yr_num = len(second_yr) # Find the number of 2nd-year students
second_yr_mw = grades.loc[(grades['Year'] == 2) & (grades['Sect'] == 'MW200')]
# Get the 2nd-year students in the MW200 section
second_yr_mw_num = len(second_yr_mw) # Find the number of 2nd-year students in the
# MW200 section
prob = second_yr_mw_num / second_yr_num # Divide to find the probability
print('The probability is %f.' % prob)

"""
# 2e
The probability is 0.321429.
"""

## 2f.

grades_sorted = grades.sort_values(by = 'CourseAve', ascending = False) # Sort the
# grades by course average, with the highest at the top
top20 = grades_sorted.loc[grades_sorted.index[0:20], 'CourseAve'] # Get the top 20
# course averages
top20_mean = np.mean(top20) # Calculate the mean
print('The mean course average for the students with the top 20 averages is %f.'
      % top20_mean)

"""
# 2f
The mean course average for the students with the top 20 averages is 95.218650.
"""

## 2g.

mw200 = grades.loc[grades['Sect'] == 'MW200'] # Get the data for the MW200 section
final_sorted = mw200.sort_values(by = 'Final') # Sort by the final exame scores,
# lowest to highest
lowest10 = final_sorted.loc[final_sorted.index[0:10], 'Final'] # Get the lowest ten
# final exam scores
print('The bottom-10 final exam scores for students in the MW200 section is:')
print(list(lowest10)) # Print a list of the lowest ten scores

"""
# 2g
The bottom-10 final exam scores for students in the MW200 section is:
[0.0, 27.5, 35.0, 40.0, 45.0, 45.0, 45.0, 45.0, 50.0, 50.0]
"""

## 2h.

apde_sorted = grades.sort_values(by = 'APDE', ascending = False) # Sort the values
# by APDE, highest to lowest
top20_apde_value = apde_sorted.loc[apde_sorted.index[112], 'APDE'] # Get the APDE
# value at the 113th position
top20_apde = apde_sorted.loc[apde_sorted['APDE'] >= top20_apde_value] # Get data
# from the top 20 percent of APDE values, accounting for ties
top20_apde_num = len(top20_apde) # Get the number of students in the top 20 percent
# for APDE

courseave_sorted = grades.sort_values(by = 'CourseAve', ascending = False)
# Sort the values by course average, highest to lowest
top20_courseave_value = courseave_sorted.loc[courseave_sorted.index[112], 'CourseAve']
# Get the course average value in the 113th position
top20_intersect = grades.loc[(grades['APDE'] >= top20_apde_value) & (grades['CourseAve'] >=
                             top20_courseave_value), :] # Get data from the top 20
# percent of APDE values and the top 20 percent of course averages, accounting for ties
top20_intersect_num = len(top20_intersect) # Get the number of students in the top
# 20 percent of both categories
perc = (top20_intersect_num / top20_apde_num) * 100 # Calculate the percentage
print('The percentage of students is %f percent.' % perc)

"""
# 2h
The percentage of students is 16.981132 percent.
"""