'''
Script to Pre-Pre Process News and Market Data
Author: Sushant Bansal <sushant@uchicago.edu>
News Source: https://components.one/datasets/all-the-news-articles-dataset/
Mareket Data Source: http://firstratedata.com/it/stock/G-L
Date: Jul 20, 2019
'''

#%% Import Statements
import pandas as pd
import numpy as np
import csv

#%% Reading In the Market Data Part 1
market_df_1 = pd.read_csv("RawData/2018_12.csv",
    names=['Date','Open','High','Low','Close'])

market_df_1.head()

#%% Reading In the Market Data Part 2

market_df_2 = pd.read_csv("RawData/2019_3.csv",
    names=['Date','Open','High','Low','Close'])

market_df_2.head()

#%% Combining the Market Data Into Together

market_df = pd.concat([market_df_1, market_df_2])
market_df.head()

#%% Sorting and Setting the Date Colum to type Datetype
market_df['Date'] = pd.to_datetime(market_df['Date'])
market_df.sort_values( by= ['Date']).head()

#%% Reading in the News
news_df = pd.read_csv("RawData/News_Title_Content_Date.csv")
news_df.head()

#%% Sorting by date and dropping unneeded columns
news_df.sort_values( by= ['date'], ascending=False).head(10)
news_df.drop(columns=['Unnamed: 0'], inplace=True)

#%% Keeping Relevant Data only [Range We Need]
market_data = market_df[(market_df['Date'] >'2017-01-01') & (market_df['Date'] <'2018-03-31')]

#%% Sanity Check
market_data.head()

#%% Keeping Relevant Only [Range We Need]
news_data = news_df[(news_df['date'] >'2017-01-01') & (news_df['date'] <'2018-03-31')]

#%% Sorting the Data
news_data = news_data.sort_values( by= ['date'], ascending=True)

#%% Saving Data As Processed Data
news_data.to_csv("ProcessedData/News_Data.csv")
market_data.to_csv("ProcessedData/Market_Data.csv", index=False)