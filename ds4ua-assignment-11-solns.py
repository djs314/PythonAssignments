## File: ds4ua-assignment-11-solns.py
## Topic: Assignment 11 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import pandas as pd # Load pandas as pd
import glob # Load glob to search for files
import datetime # Load the datetime library to work with timedelta

## 1.

filelist = glob.glob('*.csv') # Get a list of all the stocks filenames

stocks = pd.DataFrame() # Create an empty DataFrame to hold all of the stocks
for f in filelist: # loop through all the files
    newstock = pd.read_csv(f) # Get the current stock data
    newstock['Name'] = f[:-4] # Add the ticker in a new column
    stocks = pd.concat([stocks,newstock]) # Add the current stock to the bottom of the DF
stocks['Date'] = pd.to_datetime(stocks['Date']) # Convert the dates to datetime objects
stocks['Year'] = stocks['Date'].dt.year # Add the year as a column to the DF
open_dates = stocks.loc[:,['Date','Year']].drop_duplicates() # Create a DF consisting
# of the dates and years the market was open
open_dates = open_dates[(open_dates['Date'] <= '2014-12-31') & (open_dates['Date'] >= '2005-01-02')]
# Trim the open dates list to 2005-2014
open_dates.index = range(len(open_dates)) # Rename index to fix duplicate indicies for problem 6
open_dates['Year'].value_counts().sort_index() # Get the number of days the market was
# open for each year, sort by year, and print

"""
# 1
2005    252
2006    251
2007    251
2008    253
2009    252
2010    252
2011    252
2012    250
2013    252
2014    252
Name: Year, dtype: int64
"""

## 2.

missing = pd.DataFrame() # An empty DataFrame to hold the missing dates
for f in filelist: # Loop through all the stocks
    current_stock = stocks[stocks['Name'] == f[:-4]] # Get the current stock in a DF
    start = min(current_stock['Date']) # Get the earliest date in this stock
    end = max(current_stock['Date']) # Get the latest date in this stock
    current_missing = open_dates['Date'].loc[~open_dates['Date'].isin(current_stock['Date'])]
    # Get the missing dates
    current_missing = current_missing[(current_missing <= end) & (current_missing >= start)]
    # Trim the missing dates to the required range
    missing_df = pd.DataFrame() # A DataFrame to hold the missing values from this stock
    missing_df['Date'] = current_missing # Set the missing dates in the DF
    missing_df['Name'] = f[:-4] # Set the stock names in the DF
    missing = pd.concat([missing,missing_df]) # Add the missing dates and names from this
    # stock to the list of all missing dates
print('The number of missing records is %d.' % len(missing))

"""
# 2
The number of missing records is 9459.
"""

## 3.

high = missing['Name'].value_counts()[9] # Get the tenth largest number of missing records
# from a particular stock
counts_high = missing['Name'].value_counts() # Get a list of stocks and the number of
# missing records, from largest to smallest
counts_high[counts_high.values >= high] # Get and print a list of the ten stocks with
# the largest number of missing records, including ties
low = missing['Name'].value_counts(ascending=True)[9] # Get the tenth smallest number
# of missing records from a particular stock
counts_low = missing['Name'].value_counts(ascending=True) # Get a list of stocks and
# the number of missing records, from smallest to largest
counts_low[counts_low.values <= low] # Get and print a list of the ten stocks with
# the smallest number of missing records, including ties

"""
# 3
PDCO    45
FLR     44
SO      44
STJ     44
PPG     43
GE      43
RF      43
BBT     42
SWN     42
LVLT    42
HOT     42
LB      42
QCOM    42
GAS     42
Name: Name, dtype: int64
DLPH      1
MPC       3
KMI       4
VRSK      5
DISCK    10
MJN      13
PM       14
DPS      15
HBI      18
TEL      20
Name: Name, dtype: int64
"""

## 4.

stocks = stocks[(stocks['Date'] <= '2014-12-31') & (stocks['Date'] >= '2005-01-02')]
# Trim the stocks to 2005-2014
counts = stocks['Name'].groupby(stocks['Name']).apply(len) # Get the number of
# records for each stock
missing_counts = missing['Name'].groupby(missing['Name']).apply(len) # Get the
# number of missing records for each stock
counts = counts[counts.index.isin(missing_counts.index)] # Eliminate stocks that
# have no missing records from the number of records for each stock
prop = missing_counts / counts # Get the proportion of missing records for each stock
large_prop = prop.sort_values(ascending=False)[0:10] # Get the top ten proportions
# of missing records
missing_counts.loc[large_prop.index] # Get and print the number of missing records
# for the top ten proportions
small_prop = prop.sort_values()[0:10] # Get the ten smallest proportions of missing records
missing_counts.loc[small_prop.index] # Get and print the number of missing records
# for the ten smallest proportions

"""
# 4
Name
SO      44
PDCO    45
QCOM    42
STJ     44
FLR     44
GE      43
RF      43
PPG     43
GGP     41
BBT     42
Name: Name, dtype: int64
Name
DLPH      1
MPC       3
VRSK      5
KMI       4
DISCK    10
PM       14
MJN      13
DPS      15
HBI      18
OMC      26
Name: Name, dtype: int64
"""

## 5.

dates_high = missing['Date'].value_counts()[9] # Get the tenth highest number of
# missing records for a particular date
dates = missing['Date'].value_counts() # Get a list of dates and the number of
# mikssing records, from largest to smallest
dates[dates.values >= dates_high] # Get and print a list of the ten dates with
# the largest number of missing records, including ties

"""
# 5
2007-06-25    11
2005-12-15    11
2012-04-23    11
2013-01-30    10
2005-07-14    10
2011-03-08    10
2013-09-23    10
2005-02-28    10
2005-05-05    10
2006-12-04    10
Name: Date, dtype: int64
"""

## 6.

missing['Open'] = 0 # Add columns for Open, High, Low, Close, Volume, Adj Close, and
# Year, filled with zeroes (and the year for Year), so that the DataFrames will match
# up when concatenating
missing['High'] = 0
missing['Low'] = 0
missing['Close'] = 0
missing['Volume'] = 0
missing['Adj Close'] = 0
missing['Year'] = missing['Date'].dt.year
missing_final = pd.DataFrame() # A DataFrame to hold a list of missing records and their
# imputed values
for f in filelist: # Loop through all of the stocks
    current_stock = stocks[stocks['Name'] == f[:-4]] # Get the current stock's records
    current_missing = missing[missing['Name'] == f[:-4]] # Get the current stock's
    # missing dates
    for x in range(0,len(current_missing)): # Loop through each line of the missing
    # dates for this stock
        current_date = current_missing.loc[current_missing.index[x],'Date']
        post_date = current_missing.loc[current_missing.index[x],'Date']
        pre_date = current_missing.loc[current_missing.index[x],'Date']
        # Set the current missing date, and set the post date and pre date to the
        # current missing date, which will hold the next and previous open dates
        while True: # Loop until post_date is an open date
            post_date = post_date + datetime.timedelta(days=1) # Get the next date
            if post_date in list(current_stock['Date'].values):
                break # If the next date is an open date, exit the loop
        while True: # Loop until pre_date is an open date
            pre_date = pre_date - datetime.timedelta(days=1) # Get the previous date
            if pre_date in list(current_stock['Date'].values):
                break # If the previous date is an open date, exit the loop
        d3d2 = (post_date - current_date).days # Get the time differences needed for
        # the imputation formula
        d2d1 = (current_date - pre_date).days
        d3d1 = (post_date - pre_date).days
        pre = current_stock[current_stock['Date'] == pre_date] # Get the other values
        # needed for the imputation formula
        p1_open = pre.loc[pre.index[0],'Open']
        post = current_stock[current_stock['Date'] == post_date]
        p3_open = post.loc[post.index[0],'Open']
        p1_high = pre.loc[pre.index[0],'High']
        p3_high = post.loc[post.index[0],'High']
        p1_low = pre.loc[pre.index[0],'Low']
        p3_low = post.loc[post.index[0],'Low']
        p1_close = pre.loc[pre.index[0],'Close']
        p3_close = post.loc[post.index[0],'Close']
        p1_volume = pre.loc[pre.index[0],'Volume']
        p3_volume = post.loc[post.index[0],'Volume']
        current_index = current_missing[current_missing['Date'] == current_date].index
        # Fill in the values in the DF of missing dates for this stock with imputations
        current_missing.loc[current_index,'Open'] = (d3d2*p1_open + d2d1*p3_open) / d3d1
        current_missing.loc[current_index,'High'] = (d3d2*p1_high + d2d1*p3_high) / d3d1
        current_missing.loc[current_index,'Low'] = (d3d2*p1_low + d2d1*p3_low) / d3d1
        current_missing.loc[current_index,'Close'] = (d3d2*p1_close + d2d1*p3_close) / d3d1
        current_missing.loc[current_index,'Volume'] = (d3d2*p1_volume + d2d1*p3_volume) / d3d1
    missing_final = pd.concat([missing_final,current_missing]) # After looping through each line
    # of the current stock and imputating, add this stock's values to the list of all missing
    # records and their imputed values
stocks = pd.concat([stocks,missing_final]) # Add the list of missing records with imputed
# values to the list of stocks, to complete the imputation

def pythonindex(x): # A function to calculate and return the Python Index for Open, High,
# Low, and Close of a dataframe
    ser = {} # An empty set to hold the series of four values that will be returned
    mult1 = x['Open'] * x['Volume']
    num1 = mult1.sum()
    denom = x['Volume'].sum()
    ser['Open'] = num1 / denom # Calculate the Python Index for Open
    mult2 = x['High'] * x['Volume']
    num2 = mult2.sum()
    ser['High'] = num2 / denom # Calculate the Python Index for High
    mult3 = x['Low'] * x['Volume']
    num3 = mult3.sum()
    ser['Low'] = num3 / denom # Calculate the Python Index for Low
    mult4 = x['Close'] * x['Volume']
    num4 = mult4.sum()
    ser['Close'] = num4 / denom # Calculate the Python Index for Close
    return pd.Series(ser, index = ['Open', 'High', 'Low', 'Close']) # Return a Series
    # containing the Python Index for each of Open, High, Low, and Close for this DataFrame

stocks_10 = stocks[(stocks['Date'] <= '2010-10-31') & (stocks['Date'] >= '2010-10-01')]
# Get the stocks in October 2010
stocks_10.groupby(stocks_10['Date']).apply(pythonindex) # Find and print the Python Index
# for each date in October 2010
stocks['Month'] = stocks['Date'].dt.strftime('%B') # Add a column of months to the stocks
stocks['Month Year'] = stocks['Month'] + ' ' + stocks['Year'].astype(str)
# Add a column to the stocks consisting of the month and year as a string, so we can group
# by month for each year
stocks_range = stocks[(stocks['Date'] <= '2012-12-31') & (stocks['Date'] >= '2008-01-01')]
# Get the desired range of stocks in a DF
gp = stocks_range.groupby([stocks_range['Month Year'],stocks_range['Date']]).apply(pythonindex)
# Group the stocks in the desired range by month for each year, then by date, and apply
# the Python index to each date
gp.mean(axis=0,level=0) # Get the mean Python index of each of Open, High, Low, and Close
# for each month, and print

"""
# 6a
                 Open       High        Low      Close
Date                                                  
2010-10-01  39.169581  39.434530  38.461729  38.847595
2010-10-04  36.510926  36.970777  36.037449  36.470644
2010-10-05  36.821391  37.397876  36.469230  37.105123
2010-10-06  39.893535  40.348672  38.636233  39.300411
2010-10-07  38.711915  38.958309  38.004147  38.474292
2010-10-08  33.890921  34.354389  33.540042  34.078250
2010-10-11  36.729402  37.154667  36.305414  36.646461
2010-10-12  36.442557  37.035612  36.078277  36.841441
2010-10-13  36.963579  37.470745  36.601837  37.025214
2010-10-14  32.105693  32.370234  31.580260  31.928302
2010-10-15  31.384209  31.578964  30.617056  31.063536
2010-10-18  34.031321  34.490335  33.683067  34.226742
2010-10-19  33.253679  33.645777  32.673050  33.010323
2010-10-20  33.199450  33.880878  32.823187  33.527427
2010-10-21  40.940366  41.605321  40.194412  40.919451
2010-10-22  40.189095  40.802296  39.830970  40.410532
2010-10-25  35.343950  35.672289  34.925287  35.151389
2010-10-26  37.290510  38.299406  37.040847  37.953417
2010-10-27  39.112723  39.718565  38.627671  39.289454
2010-10-28  38.538390  38.825426  37.787602  38.267811
2010-10-29  39.347623  39.811310  38.935350  39.458878

#6b
                     Open       High        Low      Close
Month Year                                                
April 2008      44.443226  45.155724  43.795947  44.503364
April 2009      23.071624  23.851243  22.531289  23.285297
April 2010      36.493883  36.989883  35.956138  36.493005
April 2011      42.867418  43.353457  42.320513  42.860279
April 2012      38.646941  39.105297  38.166190  38.629491
August 2008     41.288243  42.040213  40.513061  41.308876
August 2009     28.961602  29.516990  28.487846  29.062931
August 2010     35.069629  35.561742  34.632379  35.129022
August 2011     34.352679  35.003856  33.486768  34.211051
August 2012     37.160381  37.574388  36.803358  37.204773
December 2008   26.335239  27.183410  25.544060  26.413611
December 2009   32.763814  33.119627  32.400190  32.742729
December 2010   39.662716  40.081944  39.251770  39.684723
December 2011   33.602081  34.031428  33.111160  33.537572
December 2012   37.350130  37.825887  36.975137  37.443758
February 2008   44.312511  45.094670  43.430333  44.231277
February 2009   21.604370  22.229320  20.907962  21.537163
February 2010   33.132899  33.590305  32.712490  33.230161
February 2011   42.111608  42.680693  41.621860  42.212864
February 2012   37.729617  38.218533  37.302312  37.801535
January 2008    43.879383  44.892409  42.818134  43.879455
January 2009    25.409133  26.069218  24.567002  25.308607
January 2010    32.705986  33.121490  32.155696  32.608962
January 2011    39.626213  40.106999  39.128459  39.667586
January 2012    36.615057  37.266753  36.128494  36.824483
July 2008       40.355927  41.309069  39.296554  40.294039
July 2009       26.714240  27.212668  26.268579  26.811794
July 2010       33.607538  34.101586  33.069073  33.652820
July 2011       42.172371  42.731904  41.674772  42.201682
July 2012       37.884296  38.400811  37.362617  37.910984
June 2008       43.551863  44.206226  42.731014  43.351498
June 2009       26.374804  26.816666  25.879218  26.354770
June 2010       34.969566  35.442337  34.399057  34.854441
June 2011       39.442939  39.915710  38.998463  39.428882
June 2012       35.507085  35.974332  35.038382  35.539954
March 2008      43.931635  44.795459  43.048824  43.933829
March 2009      21.135608  21.857057  20.461184  21.201853
March 2010      34.026824  34.439033  33.705850  34.099288
March 2011      42.638494  43.186795  42.078523  42.651902
March 2012      36.854072  37.273991  36.465473  36.917044
May 2008        46.223506  46.903393  45.527736  46.240284
May 2009        24.395802  25.015676  23.782373  24.428134
May 2010        34.991162  35.602147  34.217451  34.919117
May 2011        42.486394  42.965594  41.996559  42.498843
May 2012        36.616235  37.099327  36.010804  36.460415
November 2008   27.219452  28.183572  25.990354  27.058088
November 2009   32.019869  32.471559  31.640013  32.113337
November 2010   37.720691  38.234390  37.284057  37.807793
November 2011   34.096725  34.566951  33.503721  34.019407
November 2012   36.931831  37.411101  36.523875  36.988903
October 2008    31.236292  32.628599  29.519426  30.985339
October 2009    32.438632  32.937909  31.901634  32.393257
October 2010    36.660515  37.134589  36.135863  36.666509
October 2011    34.838146  35.551106  34.138827  34.922552
October 2012    38.252714  38.763395  37.739419  38.242168
September 2008  40.180907  41.356652  38.654772  39.998303
September 2009  30.872073  31.393763  30.383100  30.899522
September 2010  36.286588  36.778156  35.907844  36.384822
September 2011  37.009378  37.650239  36.107664  36.725012
September 2012  37.713443  38.147519  37.328751  37.760984
"""