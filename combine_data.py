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

import multiprocessing as mp

#%% Reading In the Market Data | Frequency : Minute
minute_market_df = pd.read_csv("ProcessedData/Pre_Market_Data.csv")
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

#%% Adding Movements Columns
daily_market_df['OpenDiff'] = daily_market_df['Open'] - daily_market_df['Open'].shift(1)
daily_market_df['CloseDiff'] = daily_market_df['Close'] - daily_market_df['Close'].shift(1)
daily_market_df.head(10)

#%% Assigning Positive Movement 1 and Negative Movement 0
daily_market_df['OpenMove']=np.clip(np.sign(daily_market_df['OpenDiff']), 0, None)
daily_market_df['CloseMove']=np.clip(np.sign(daily_market_df['CloseDiff']), 0, None)
daily_market_df.head()

#%% Readding the Date to Help us Join with Market Data

daily_market_df['Date'] = pd.to_datetime(daily_market_df[['Day', 'Month', 'Year']])
daily_market_df.head()
#%%

news_data_df = pd.read_csv("ProcessedData/Pre_News_Data.csv")
news_data_df.drop(columns=['Unnamed: 0'], inplace=True)
news_data_df.head()

#%% Dropping All the NaNs
print("NaN Summary in Daily Market Data: \n", daily_market_df.isna().sum())
daily_market_df.dropna(inplace=True)
print("\nNaN Summary in Daily News Data: \n", news_data_df.isna().sum())
news_data_df.dropna(inplace=True)


#%% Finding All Malformed Dates  in the dataframe
n_threads = mp.cpu_count() - 1

splits = np.array_split(news_data_df, n_threads)

def error_dates(df):
    res = []
    for index, _ in df.iterrows():
        try:
            pd.to_datetime(news_data_df.iloc[index,1])
        except:
            res.append(index)
    
    return res

pool = mp.Pool(n_threads)

err_dates = pool.map(error_dates, splits)

pool.close()

#%% Dropping All the rows With Malformed Dates
err_dates = np.concatenate(err_dates)
print("Number of Malicious Dates", err_dates.shape[0])
news_data_df.drop(err_dates, inplace=True)

#%% Convertinf the Date Column in News Data to date time
news_data_df['date'] = pd.to_datetime(news_data_df['date'])

#%% Converting from Object type to pandas datetime format 
sorted_news_data  = news_data_df.sort_values(by=['date']).reset_index(drop=True)
sorted_news_data.columns = ['Title', 'Date', 'Content']
sorted_news_data.head()

#%% Only Keeping the Columns Needed to Join
sorted_market_df = daily_market_df[['Date', 'OpenMove', 'CloseMove']]
sorted_market_df.head()

#%% Joing the News and the Market Data
combined_df = pd.merge(sorted_news_data, sorted_market_df, on='Date', how='left') 
combined_df.dropna(inplace=True)
#%% Resetting the index
combined_df.reset_index(drop=True, inplace=True)

#%% Saving Combined Data to A File

combined_df.to_csv("ProcessedData/CombinedData.csv")