'''
Script to Combine The Market Data and News Data 
along with some more processing
Author: Sushant Bansal <sushant@uchicago.edu>
Date: Jul 22, 2019
'''
#%% Imports
import pandas as pd
import numpy as np
import csv

from sklearn.preprocessing import MinMaxScaler

#%% Reading In the Market Data | Frequency : Minute
minute_market_df = pd.read_csv("ProcessedData/Market_Data.csv")
minute_market_df.head()

#%% Converting date from Object to Datetime to help in processing
minute_market_df['Date'] = pd.to_datetime(minute_market_df['Date'])

#%% Seperating Out Dattime into Components

minute_market_df['Day']  = pd.DatetimeIndex(minute_market_df['Date']).day
minute_market_df['Month']  = pd.DatetimeIndex(minute_market_df['Date']).month
minute_market_df['Year']  = pd.DatetimeIndex(minute_market_df['Date']).year
minute_market_df['Hour']  = pd.DatetimeIndex(minute_market_df['Date']).hour
minute_market_df['Minute']  = pd.DatetimeIndex(minute_market_df['Date']).minute

minute_market_df.head()


#%% Getting Opening and Closing Prices

daily_market_df = pd.DataFrame()

daily_market_df['Day'] = minute_market_df[(minute_market_df['Hour'] == 9) & (minute_market_df['Minute'] == 30)]['Day']

daily_market_df['Month'] = minute_market_df[(minute_market_df['Hour'] == 9) & (minute_market_df['Minute'] == 30)]['Month']

daily_market_df['Year'] = minute_market_df[(minute_market_df['Hour'] == 9) & (minute_market_df['Minute'] == 30)]['Year']

daily_market_df['Open'] =  minute_market_df[(minute_market_df['Hour'] == 9) & (minute_market_df['Minute'] == 30)]['Open']

daily_market_df.reset_index(drop=True, inplace=True)

daily_market_df['Close'] = minute_market_df[(minute_market_df['Hour'] == 15) & (minute_market_df['Minute'] == 59)]['Close'].reset_index(drop=True)

daily_market_df.head(25)

#%% [markdown]
# * Drop High and Low Columns from the Daily Set \\
# * Min-Max Normalize the data NOT NEEDED \\
# * Add Open Diff and Close Diff Columns \\
# * Start Joining the News with data

#%%
daily_market_df['OpenDiff'] = daily_market_df['Open'] - daily_market_df['Open'].shift(1)
daily_market_df['CloseDiff'] = daily_market_df['Close'] - daily_market_df['Close'].shift(1)

daily_market_df.head(10)

#%%

#%%

#%%


#%%
