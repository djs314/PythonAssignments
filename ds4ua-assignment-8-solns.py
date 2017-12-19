## File: ds4ua-assignment-8-solns.py
## Topic: Assignment 8 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import pandas as pd # Load pandas as pd
reviews = pd.read_csv('reviews.txt', 
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date'])
# Read in the DataFrame

## 1a.

oldest_date = reviews['Date'].min() # Get the UTC for the oldest date
newest_date = reviews['Date'].max() # Get the UTC for the newest date
od = pd.to_datetime(oldest_date, unit='s') # Convert the UTC for the oldest date
# to a datetime object
nd = pd.to_datetime(newest_date, unit='s') # Convert the UTC for the newest date
# to a datetime object
print('The date and time of the oldest review is', od)
print('The date and time of the most recent review is', nd)

"""
# 1a
The date and time of the oldest review is 1997-09-20 03:05:10
The date and time of the most recent review is 1998-04-22 23:10:38
"""

## 1b.

format = "%A %B %d %Y %H:%M:%S" # Create a format string for the output
median_date = reviews['Date'].median() # Get the median UTC
md = pd.to_datetime(median_date, unit='s') # Convert the median UTC to a datetime object
print('The median date and time for the reviews is', md.strftime(format))
# Print the median datetime as a formatted string

"""
# 1b
The median date and time for the reviews is Monday December 22 1997 21:42:24
"""

## 1c.

dates = pd.to_datetime(reviews['Date'], unit='s') # Get a Series of datetime objects
# for all of the UTC codes
reviews['Month'] = dates.dt.month # Add a column called 'Dates' to the DataFrame
# consisiting of the months for each review
month_gp = reviews['Rating'].groupby(reviews['Month']) # Group the ratings by the
# months that they occurred in
month_gp.mean() # Calculate and print the average rating for each month

"""
# 1c
Month
1     3.397730
2     3.455009
3     3.548831
4     3.574848
9     3.540125
10    3.591421
11    3.559842
12    3.580388
Name: Rating, dtype: float64
"""

## 1d.

reviews['DayOfWeek'] = dates.dt.strftime('%A') # Add a column called 'DayOfWeek' to
# the DataFrame consisting of the day of the week for each review
week_gp = reviews['Rating'].groupby(reviews['DayOfWeek']) # Group the ratings by
# the day of the week each occurred
week_gp.count().sort_values(ascending=False).index[0] # Count the number of ratings
# for each day of the week, and report the day of the week that had the highest number
# of ratings

"""
# 1d
'Wednesday'
"""

## 1e.

reviewer_gp = reviews['Date'].groupby(reviews['Reviewer']) # Group the dates by
# each reviewer
five_reviewers = reviewer_gp.count().sort_values(ascending=False).index[0:5]
# Get the five reviewers who had the most reviews
for rev in five_reviewers:# For each of the top 5 reviewers, do the following:
    rev_dates = reviews[reviews['Reviewer'] == rev] # Get the dates for the reviewer
    rev_first = rev_dates['Date'].min() # get the date of the first review for the reviewer
    rf = pd.to_datetime(rev_first, unit='s') # Convert the UTC to a datetime object
    print('The first review of reviewer', rev, 'was on', rf)

"""
# 1e
The first review of reviewer 405 was on 1998-01-23 08:37:15
The first review of reviewer 655 was on 1998-02-14 02:52:00
The first review of reviewer 13 was on 1997-12-07 17:11:23
The first review of reviewer 450 was on 1997-12-15 19:53:37
The first review of reviewer 276 was on 1997-09-20 20:12:17
"""

lines = pd.Series(open('pizza_requests.txt').read().splitlines())

## 2a.

utc = pd.DataFrame(lines[lines.str.contains('unix_timestamp_of_request_utc')].str.split().str[1],
                         columns = ['Date']) # Create a DataFrame with a 'Date' column
                         # consisting of the UTC codes
oldest_date = utc['Date'].min() # Get the UTC for the oldest date
newest_date = utc['Date'].max() # Get the UTC for the newest date
od = pd.to_datetime(oldest_date, unit='s') # Convert the UTC for the oldest date
# to a datetime object
nd = pd.to_datetime(newest_date, unit='s') # Convert the UTC for the newest date
# to a datetime object
print('The date and time of the oldest request is', od)
print('The date and time of the most recent request is', nd)

"""
# 2a
The date and time of the oldest request is 2011-02-14 22:28:57
The date and time of the most recent request is 2013-10-12 01:30:36
"""

## 2b.

median_date = utc['Date'].median() # Get the median UTC
md = pd.to_datetime(median_date, unit='s') # Convert the median UTC to a datetime object
print('The median date and time for the reviews is', md.strftime(format))
# Print the median datetime as a formatted string

"""
# 2b
The median date and time for the reviews is Friday July 20 2012 17:54:08
"""

## 2c.

dates = pd.to_datetime(utc['Date'], unit='s') # Convert the column of UTC codes to a
# Series of datetime objects
utc['Hour'] = dates.dt.hour # Add a column called 'Hour' to the DataFrame consisting
# of the hour each request occurred
hour_gp = utc['Date'].groupby(utc['Hour']) # Group the dates by the hour each occurred
hour_gp.count().sort_values(ascending=False).iloc[0:5] # Report the five one-hour periods
# with the most requests

"""
# 2c
Hour
0     508
22    497
23    491
21    464
1     441
Name: Date, dtype: int64
"""

## 2d.

pizza = lines[lines.str.contains('requester_received_pizza')].str.split().str[1]
# Get the 'true' or 'false' indicators of whether a user received pizza
utc['Pizza'] = pizza.values # Add those indicators in a new column of the DateFrame
# called "Pizza'

def prop(x): # A function that returns the proportion of successful pizza requests in
# a DataFrame
    pro = x['Pizza'].loc[x['Pizza'].values == 'true'].count() / x['Pizza'].count()
    # Calculate the proportion of successful pizza requests in DataFrame x
    return pro # Return the proportion

prop_gp = utc.groupby(utc['Hour']) # Group the DataFrame by hour
props = prop_gp.apply(prop) # Apply the function prop to each hour to get the proportion
# of successful pizza requests for each hour
high_prop = props.sort_values(ascending=False).index[0] # Get the hour that has the
# highest proportion of successful pizza requests
print('Hour %d had the highest proportion of successful pizza requests.' % high_prop)

"""
# 2d
Hour 13 had the highest proportion of successful pizza requests.
"""

## 2e.

low_prop = props.sort_values().index[0] # Get the hour that has the lowest proportion
# of successful pizza requests
print('Hour %d had the lowest proportion of successful pizza requests.' % low_prop)

"""
# 2e
Hour 8 had the lowest proportion of successful pizza requests.
"""