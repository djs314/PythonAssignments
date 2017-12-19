## File: ds4ua-assignment-7-solns.py
## Topic: Assignment 7 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import numpy as np # Load numpy as np
import pandas as pd # Load pandas as pd

lines = pd.Series(open('pizza_requests.txt').read().splitlines()) # Load the lines
# of the text file into a Series

## 1.

all_requests = lines[lines.str.contains('requester_received_pizza')] # Get all lines
# with 'requester_received_pizza'
num_requests = len(all_requests) # Count the total number of requests
num_got_pizza = len(all_requests[all_requests.str.contains('true')]) # Count the number
# of successful requests
pizza_prop = num_got_pizza / num_requests # Get the proportion of successful requests
print('The proportion of successful requests is %f.' % pizza_prop)

"""
# 1
The proportion of successful requests is 0.246341.
"""

## 2.

age = lines[lines.str.contains('requester_account_age_in_days_at_request')].str.split().str[1]
# Get the account ages at the time of request
age = age.astype(float) # Convert the ages to floating-point numbers
median_age = np.median(age) # Get the median account age
print('The median account age at the time of request is %f.' % median_age)

"""
# 2
The median account age at the time of request is 155.647593.
"""

## 3.

n1 = len(age[age > median_age]) # Count the number of older accounts
n2 = len(age[age <= median_age]) # Count the number of newer accounts
x1 = 0 # A variable to hold the number of successful requests from older accounts
for i in range(num_requests): # Loop through all of the requests
    if (age.iloc[i] > median_age) and (all_requests.iloc[i].count('true') > 0):
        x1 += 1 # If the ith request is from an older account and was successful,
        # increase the count by 1
p1 = x1 / n1 # Calculate the proportion
x2 = 0
for i in range(num_requests): # Loop through all of the requests
    if (age.iloc[i] <= median_age) and (all_requests.iloc[i].count('true') > 0):
        x2 += 1 # If the ith request is from a newer account and was successful,
        # increase the count by 1
p2 = x2 / n2 # Calculate the proportion
lower = p1 - p2 - 1.96*(((p1*(1-p1)/n1) + (p2*(1-p2)/n2))**0.5) # Get the lower bound
upper = p1 - p2 + 1.96*(((p1*(1-p1)/n1) + (p2*(1-p2)/n2))**0.5) # Get the upper bound
print('The confidence interval is (%f, %f).' % (lower, upper))

"""
# 3
The confidence interval is (0.021771, 0.066571).
"""

## 4.

request_text = lines[lines.str.contains('\"request_text\"')] # Get all of the request texts
ct = 0 # A variable to hold the number of requests that mention 'student' or 'children'
for i in range(num_requests): # Loop through all of the requests
    if (request_text.iloc[i].lower().count('student') > 0) or (request_text.iloc[i].
    lower().count('children') > 0):
        ct += 1 # If the ith request mentions 'student' or 'children', increase the count
        # by 1
perc = 100 * (ct / num_requests) # Calculate the percentage
print('%f percent of requests mention \'student\' or \'children\'.' % perc)

"""
# 4
9.222359 percent of requests mention 'student' or 'children'.
"""

## 5.

request_title = lines[lines.str.contains('\"request_title\"')] # Get all of the request titles
ct = 0 # A variable to hold the number of requests from Canada
for i in range(num_requests): # Loop through all of the requests
    if request_title.iloc[i].lower().count('canada') > 0:
        ct += 1 # If the ith request title mentions 'Canada', increase the count by 1
print('%d requests are from Canada.' % ct)

"""
# 5
103 requests are from Canada.
"""

## 6.

giver = lines[lines.str.contains('giver_username_if_known')] # Get all of the giver
# usernames
x = 0 # A variable to hold the number of successful pizza requests donated anonomously
for i in range(num_requests): # Loop through all of the requests
    if (all_requests.iloc[i].count('true') > 0) and (giver.iloc[i].count('\"N/A\"') > 0):
        x += 1 # If the its request is successful and anonomous, increment the counter
        # by 1
p = x / num_got_pizza # Calculate the proportion
lower = p - 1.96*((p*(1-p)/num_got_pizza)**0.5) # Get the lower bound of the CI
upper = p + 1.96*((p*(1-p)/num_got_pizza)**0.5) # Get the upper bound of the CI
print('The confidence interval is (%f, %f).' % (lower, upper))

"""
# 6
The confidence interval is (0.689967, 0.737377).
"""

## 7.

num_s = lines[lines.str.contains('requester_number_of_subreddits_at_request')].str.split().str[1]
# Get all of the numbers of user's subreddits
num_s = num_s.astype(int) # Convert the numbers to integers
max_s = num_s.max() # Get the maximum number of subreddits a user is subscribed to
print('The maximum number of subreddits subscribed to by a single user is %d.' % max_s)

"""
# 7
The maximum number of subreddits subscribed to by a single user is 235.
"""

## 8.

subreddits = [] # A list to hold the subreddits
for line in lines: # Loop through all lines of the text file
    if line.startswith('  \"'):
        subreddits.append(line.strip()) # For each subreddit, append it to the list
subreddits = pd.Series(subreddits) # Convert the list to a Series to use value_counts
num_sub = len(subreddits.unique()) # Get the number of distinct subreddits
print('There are %d distinct subreddits.' % num_sub)
subreddits.value_counts().to_csv('ds4ua-assignment07-subreddits.txt') # Print the
# subreddits and their counts to a text file

"""
# 8
There are 9404 distinct subreddits.
"AskReddit"               3241
"pics"                    2734
"funny"                   2704
"IAmA"                    2138
"WTF"                     2133
"gaming"                  2079
"Random_Acts_Of_Pizza"    1978
"videos"                  1620
"todayilearned"           1556
"AdviceAnimals"           1452
"""