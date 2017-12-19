## File: ds4ua-assignment-6-solns.py
## Topic: Assignment 6 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


alllines = open('timing_log.txt').read().splitlines() # Open the text file, storing
# the lines in a list

import numpy as np # Import numpy as np
import pandas as pd # Import pandas as pd

## 1.

ct = 0 # A counter variable to hold the number of requests for a PDF version
for line in alllines: # Loop through each line of the text file
    if line.count('hardcopy') > 0:
        ct += 1 # For each line, check if it contains the string 'hardcopy', and if
                # it does, increase the count by 1. This string should only appear in
                # the WeBWork element, so we don't need to worry about overcounting. 
print('The number of requests for a PDF version of an assignment is %d.' % ct)

"""
# 1
The number of requests for a PDF version of an assignment is 138.
"""

## 2.

ct = 0 # A counter variable to hold the number of entries for STAT 2120
for line in alllines: # Loop through each line of the text file
    if line.count('STAT2120') > 0:
        ct += 1 # For each line, check if it contains the string 'STAT2120', and if
                # it does, increase the count by 1.
perc = 100 * (ct / len(alllines)) # Calculate the percentage of STAT 2120 entries
print('%f percent of the log entries were for STAT 2120.' % perc)

"""
# 2
52.492439 percent of the log entries were for STAT 2120.
"""

## 3.

weblines = [] # A list to hold the WeBWork elements
for line in alllines: # Loop through each line of the text file
    weblines.append(line.split()[8]) # For each line, get the WeBWork element, and
    # add it to the list
ct = 0 # A counter variable to hold the number of log entires that were initial log ins
test = []
for line in weblines: # Loop through each WeBWork element
    if ((line.count('/') == 2) and (not line.endswith('/]'))) or ((line.count('/')
    == 3) and (line.endswith('/]'))):
        # For each element, check whether it only has two entires, which are 'webwork2'
        # and the class name
        ct += 1 # Increment the counter if we have a correct log entry
        test.append(line)
perc = 100 * (ct / len(alllines)) # Calculate the percentage
print('%f percent of the log entries came from the student\'s initial log in.' % perc)

"""
# 3
3.792106 percent of the log entries came from the student's initial log in.
"""

## 4.

ct = 0
for line in weblines: # Loop through each line of the WeBWork elements
    if (line.count('/') >= 4) or ((line.count('/') == 3) and (not line.endswith('/]'))):
        if (line.split('/')[3] == 'instructor') or (line.split('/')[3] == 'instructor]'):
            ct += 1
print('The number of log entries from instructors peforming administrative tasks is %d.'
      % ct)

"""
# 4
The number of log entries from instructors peforming administrative tasks is 295.
"""

## 5.

def most_common(x): # A function that finds the most common element of a list, ignoring
    # ties
    counts = [] # A list to hold the number of times each element in x appears
    for element in x: # Loop through each element of x
        counts.append(x.count(element)) # Add the number of times each element appears
        # to the list
    max_ct = max(counts) # Get the number of times the most common element appears
    for element in x: # Loop througb each element of x
        if x.count(element) == max_ct: # Check if each element is the most common element
            return element # Return the most common element

def least_common(x): # A function that finds the least common element of a list, ignoring
    # ties
    counts = [] # A list to hold the number of times each element in x appears
    for element in x: # Loop through each element of x
        counts.append(x.count(element)) # Add the number of times each element appears
        # to the list
    min_ct = min(counts) # Get the number of times the most common element appears
    for element in x: # Loop through each element of x
        if x.count(element) == min_ct: # Check if each element is the least common element
            return element # Return the least common element

timelines = [] # A list to hold the times
for line in alllines: # Loop through all lines in the text file
    timelines.append(line.split()[3]) # Add the time of each line to the list
hourlines = [] # A list to hold the hour of day
for line in timelines: # Loop through all of the times
    hourlines.append(line.split(':')[0]) # Add the hour of day to the list
print('The hour of the day that had the most log entries is %s.' % most_common(hourlines))
# Find the most common hour of day and print
print('The hour of the day that had the least log entries is %s.' % least_common(hourlines))
# Find the least common hour of day and print

"""
# 5
The hour of the day that had the most log entries is 22.
The hour of the day that had the least log entries is 06.
"""

## 6.

classes = [] # A list to hold the classes
for line in weblines: # Loop through all of the WeBWork elements
    if (line.count('/') >= 3):
        classes.append(line.split('/')[2]) # For each line conatining a class name
        # followed by '/', add that class name to the list
    if (line.count('/') == 2) and (not line.endswith('/]')):
        line_trunc = line.split(']')[0] # For each line containing a class name followed
        # by ']', remove the ']'
        classes.append(line_trunc.split('/')[2]) # Then, add the class name to the list
classes_unique = np.unique(classes) # Get a list of the unique classes
print('There are %d different classes that use the system.' % len(classes_unique))
# Get the number of different class and print

"""
# 6
There are 40 different classes that use the system.
"""

## 7.

def get_num_entries(x): # A function that finds the number of entries of a particular class
    ct = 0 # A counter variable to hold the number of entries
    for line in alllines: # Loop through all lines of the text file
        if (line.count(x + '/') > 0) or (line.count(x + ']') > 0):
            ct += 1 # For each line, check if it is for the class x. If so, increment
            # the counter by 1.
    return ct # Return the number of log entries

def get_runtime(x): # A function that finds the total runtime for a particular class
    num = 0 # A variable to hold the total runtime
    for line in alllines: # Loop through all lines of the text file
        if (line.count(x + '/') > 0) or (line.count(x + ']') > 0):
            num += float(line.split()[11]) # For each line, check if it is for the class x.
            # If so, add the runtime for that line to the total.
    return num # Return the total runtime

def top_three(x): # A function that returns the top three values of a numerical list
    top = [] # A list to hold the top three values
    temp = list(x) # Copy the list to a temporary variable so that we do not change
    # the original
    i = 0 # A counter for the loop
    while i < 3: # Loop through this code three times
        top.append(max(temp)) # Add the current maximum value to the list
        temp.remove(max(temp)) # Remove the current maximum value so that we can get the
        # next one
        i += 1 # Increment the counter
    return top # Return the top three values

num_entries = [] # A list to hold the number of entries of each class
runtime = [] # A list to hold the total runtimes of each class
top3_classes_entries = [] # A list to hold the three classes with the most entries
top3_classes_runtime = [] # A list to hold the three classes with the highest runtimes
for line in classes_unique: # Loop through the classes
    num_entries.append(get_num_entries(line)) # Add the number of entries of each class
    # to the list
for line in classes_unique: # Loop through the classes
    runtime.append(get_runtime(line)) # Add the total runtimes of each class to the list
top3_entries = top_three(num_entries) # Find the three highest number of entries
top3_runtime = top_three(runtime) # Find the three longest total runtimes
for entry in top3_entries: # Loop through the three highest number of entries
    for line in classes_unique: # For each number of entries, loop through all the classes
        if entry == get_num_entries(line): # Check if the current number of entries
        # equals the number of entries for the current class
            top3_classes_entries.append(line) # If so, add the class to the list
for time in top3_runtime: # Loop through the three longest runtimes
    for line in classes_unique: # For each runtime, loop through all the classes
        if time == get_runtime(line): # Check if the current total runtime equals
        # the runtime for the current class
            top3_classes_runtime.append(line) # If so, add the class to the list
print('The three classes with the highest number of log entries, from highest to lowest, are:')
print(list(top3_classes_entries)) # Print the three classes with the highest number of
# entries
print('The three classes with the highest total runtime, from highest to lowest, are:')
print(list(top3_classes_runtime)) # Print the three classes with the longest runtimes

"""
# 7
The three classes with the highest number of log entries, from highest to lowest, are:
['Spring11-STAT2120', 'Spring12-STAT2120', 'Spring11-APMA2130-Fulgham']
The three classes with the highest total runtime, from highest to lowest, are:
['Spring11-STAT2120', 'Spring11-APMA2130-Fulgham', 'Spring12-APMA2130']
"""

## 8.

ave_runtime = [] # A list to hold the average runtimes of each class
top3_classes_ave_runtime = [] # A list to hold the three classes with the largest average
# runtimes
for line in classes_unique: # Loop through each class
    ave_runtime.append(get_runtime(line) / get_num_entries(line)) # For each class, add
    # the average runtime to the list
top3_ave_runtime = top_three(ave_runtime) # Get the top three average runtimes
for ave_time in top3_ave_runtime: # Loop through the three largest average runtimes
    for line in classes_unique: # For each runtime, loop through all the classes
        if ave_time == get_runtime(line) / get_num_entries(line): # Check if the current
        # average runtime equals the average runtime for the current class
            top3_classes_ave_runtime.append(line) # If so, add the class to the list
print('The three classes with the largest average runtimes, from highest to lowest, are:')
print(list(top3_classes_ave_runtime)) # Print the three classes with the largest average
# runtimes
print('And their corresponding average runtimes are:')
print(list(top3_ave_runtime)) # Print the three largest average runtimes

"""
# 8
The three classes with the largest average runtimes, from highest to lowest, are:
['APMA2120-Devel', 'apma2130-devel', 'Spring12-APMA2130']
And their corresponding average runtimes are:
[0.5334690265486726, 0.3876734693877551, 0.34805043149946097]
"""

## 9.

ct = 0 # A counter variable to hold the number of problems
problems = [] # A list to hold the problems, used for part 10
for line in weblines: # Loop through all of the WeBWork elements
    if (line.count('/') >= 5) or ((line.count('/') == 4) and (not line.endswith('/]'))):
    # Check if the element contains a fourth element, where the class number would appear
        if (str.isdigit(line.split('/')[4])) or (str.isdigit(line.split('/')[4][:-1])
        and line.split('/')[4].endswith(']')):
        # Check if the fourth element is a problem number, and thus the line is a problem
            problems.append(line) # If so, add the line to the list
            ct += 1 # Increase the counter by 1
perc = 100 * (ct / len(alllines)) # Calculate the percentage
print('%f percent of log entries were accessing a problem.' % perc)

"""
# 9
78.507926 percent of log entries were accessing a problem.
"""

## 10.

prob_most = [] # A list to hold the most common problems
prob_counts = pd.Series(problems).value_counts() # Get the most common problems
# and the number of times each appears
i = 0 # A counter variable to index on the problems to check for ties
while(True): # Loop until two problems have different counts
    prob_most.append(prob_counts.index[i]) # Add the current most common problem
    # to the list
    if prob_counts.values[i] != prob_counts.values[i+1]: # Check if the current
    # most common problem is different from the next most common problem
        break # If so, exit the loop
    i += 1 # If not, increment the counter and repeat
print('The problem(s) with the most log entries is/are:')
print(prob_most)

"""
# 10
The problem(s) with the most log entries is/are:
['[/webwork2/Spring11-STAT2120/Webwork09/22/]']
"""