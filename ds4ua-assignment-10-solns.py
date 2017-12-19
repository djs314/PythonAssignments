## File: ds4ua-assignment-10-solns.py
## Topic: Assignment 10 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import pandas as pd # Load pandas as pd
import glob # Load glob to search for files

## 1.

filelist = glob.glob('*.csv') # Get a list of all the stocks filenames

stocks = pd.DataFrame() # Create an empty DataFrame to hold all of the stocks
for f in filelist: # loop through all the files
    newstock = pd.read_csv(f) # Get the current stock data
    newstock['Name'] = f[:-4] # Add the ticker in a new column
    stocks = pd.concat([stocks,newstock]) # Add the current stock to the bottom of the DF

open_ave = stocks['Open'].mean() # Get the mean of Open for all stocks
high_ave = stocks['High'].mean() # Get the mean of High for all stocks
low_ave = stocks['Low'].mean() # Get the mean of Low for all stocks
close_ave = stocks['Close'].mean() # Get the mean of Close for all stocks
print('The mean of the Open entries is %f.' % open_ave)
print('The mean of the High entries is %f.' % high_ave)
print('The mean of the Low entries is %f.' % low_ave)
print('The mean of the Close entries is %f.' % close_ave)

"""
# 1
The mean of the Open entries is 50.863852.
The mean of the High entries is 51.459412.
The mean of the Low entries is 50.253368.
The mean of the Close entries is 50.876482.
"""

## 2.

close_gp = stocks['Close'].groupby(stocks['Name']) # Group the Close values by the
# stock
close_mean = close_gp.mean() # Get the mean of Close for each stock
close_sort = close_mean.sort_values(ascending=False) # Sort the values from largest
# to smallest
close_sort[0:5] # Get the five stocks with the largest Close means
close_sort[-5:] # Get the five stocks with the smallest Close means

"""
# 2
Name
CME     253.956017
AZO     235.951950
AMZN    185.140534
BLK     164.069088
GS      139.146781
Name: Close, dtype: float64
Name
HBAN    13.697483
ETFC    12.808103
XRX     11.291864
F       11.174158
FTR      8.969515
Name: Close, dtype: float64
"""

## 3.

stocks['Vol'] = stocks['High'] - stocks['Low'] # Find the difference between High and Low
# and add it as a new column called 'Vol' to the DataFrame
vol_gp = stocks['Vol'].groupby(stocks['Name']) # Group the Volatility by the stock
vol_ave = vol_gp.mean() # Get the mean volatility for each stock
vol_sort = vol_ave.sort_values(ascending=False) # Sort the values from largest to smallest
vol_sort[0:5] # Get the five stocks with the largest average volatility
vol_sort[-5:] # Get the five stocks with the smallest average volatility

"""
# 3
Name
CME     7.697287
AMZN    4.691407
BLK     4.470693
AZO     4.330294
ICE     4.056189
Name: Vol, dtype: float64
Name
NI      0.363250
HBAN    0.343893
F       0.323567
XRX     0.308743
FTR     0.205275
Name: Vol, dtype: float64
"""

## 4.

stocks['RelVol'] = stocks['Vol'] / (0.5 * (stocks['Open'] + stocks['Close']))
# Calculate the relative volatility and add it as a new column called 'RelVol' to the DF
relvol_gp = stocks['RelVol'].groupby(stocks['Name']) # Group the relative volatility by
# the stock
relvol_ave = relvol_gp.mean() # Get the average relative volatility for each stock
relvol_sort = relvol_ave.sort_values(ascending=False) # Sort the values from largest
# to smallest
relvol_sort[0:5] # Get the five stocks with the largest average relative volatility
relvol_sort[-5:] # Get the five stocks with the smallest average relative volatility

"""
# 4
Name
AAL     0.055533
LVLT    0.054870
EQIX    0.051295
REGN    0.048172
ETFC    0.045381
Name: RelVol, dtype: float64
Name
WEC    0.015761
CL     0.015521
K      0.014992
PG     0.014192
GIS    0.013966
Name: RelVol, dtype: float64
"""

## 5.

stocks['Date'] = pd.to_datetime(stocks['Date']) # Convert the dates to datetime objects
# so we can work with them
feb_stocks = stocks[(stocks['Date'] <= '2010-02-28') & (stocks['Date'] >= '2010-02-01')]
# Get the stocks in February 2010
feb_open = feb_stocks['Open'].mean() # Get the mean of Open for all stocks in Feb 2010
feb_high = feb_stocks['High'].mean() # Get the mean of High for all stocks in Feb 2010
feb_low = feb_stocks['Low'].mean() # Get the mean of Low for all stocks in Feb 2010
feb_close = feb_stocks['Close'].mean() # Get the mean of Close for all stocks in Feb 2010
feb_volume = feb_stocks['Volume'].mean() # Get the mean of Volume for all stocks in Feb 2010
print('The average Open price in February 2010 is %f.' % feb_open)
print('The average High price in February 2010 is %f.' % feb_high)
print('The average Low price in February 2010 is %f.' % feb_low)
print('The average Close price in February 2010 is %f.' % feb_close)
print('The average volume in February 2010 is %f.' % feb_volume)

"""
# 5
The average Open price in February 2010 is 42.695303.
The average High price in February 2010 is 43.203673.
The average Low price in February 2010 is 42.200830.
The average Close price in February 2010 is 42.804060.
The average volume in February 2010 is 7416516.797548.
"""

## 6.

stocks_12 = stocks[stocks['Date'].dt.year == 2012] # Get the stocks in the year 2012
date_gp = stocks_12['RelVol'].groupby(stocks_12['Date']) # Group the relative volatility
# by the dates
date_ave = date_gp.mean() # Get the mean relative volatility for each date
date_sort = date_ave.sort_values(ascending=False) # Sort the values from largest
# to smallest
date_max = date_sort.index[0] # Get the date with the largest average relative volatility
date_min = date_sort.index[-1] # Get the date with the smallest average relative volatility
print('The date with the maximum average relative volatility is', date_max.strftime("%B %d %Y"))
print('The date with the minimum average relative volatility is', date_min.strftime("%B %d %Y"))

"""
# 6
The date with the maximum average relative volatility is June 21 2012
The date with the minimum average relative volatility is December 24 2012
"""

## 7.

stocks_813 = stocks[(stocks['Date'] <= '2013-12-31') & (stocks['Date'] > '2008-01-01')]
# Get the stocks between 2008 and 2013
stocks_813['DayofWeek'] = stocks_813['Date'].dt.strftime('%A') # Add a column called
# 'DayofWeek' containing the day of the week for each entry
day_gp = stocks_813['RelVol'].groupby(stocks_813['DayofWeek']) # Group the relative
# volatility by the day of the week
day_gp.mean() # Get and print the average relative volatility for each day of the week

"""
# 7
DayofWeek
Friday       0.029041
Monday       0.028542
Thursday     0.031066
Tuesday      0.029436
Wednesday    0.029766
Name: RelVol, dtype: float64
"""

## 8.

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
python_gp = stocks_10.groupby(stocks_10['Date']) # Group the DataFrame by the date
python_gp.apply(pythonindex) # Find and print the Python Index for each date

"""
# 8
                 Open       High        Low      Close
Date                                                  
2010-10-01  39.272779  39.540464  38.574467  38.961689
2010-10-04  36.513664  36.973598  36.039906  36.473198
2010-10-05  36.868819  37.448798  36.515236  37.154517
2010-10-06  40.069422  40.526281  38.790438  39.453984
2010-10-07  38.738979  38.982299  38.023149  38.494185
2010-10-08  33.953131  34.418515  33.601610  34.141493
2010-10-11  36.415035  36.840357  35.996804  36.331342
2010-10-12  36.550699  37.148552  36.185750  36.956121
2010-10-13  36.769845  37.277431  36.410377  36.830507
2010-10-14  31.929174  32.188759  31.399433  31.746258
2010-10-15  31.379396  31.574286  30.611508  31.058207
2010-10-18  34.735203  35.208943  34.389509  34.947873
2010-10-19  33.418144  33.812511  32.833834  33.171654
2010-10-20  33.225863  33.908320  32.849706  33.555329
2010-10-21  40.968005  41.634092  40.219655  40.945613
2010-10-22  40.206448  40.821101  39.843407  40.424731
2010-10-25  35.196479  35.525335  34.779042  35.002647
2010-10-26  37.425957  38.443149  37.176602  38.095958
2010-10-27  40.800620  41.430831  40.293345  40.981265
2010-10-28  38.377249  38.645428  37.617353  38.085284
2010-10-29  40.159713  40.638799  39.741861  40.279059
"""