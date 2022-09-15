# imprt required packages
import pandas as pd
from aplha_vantage.timeseries import TimeSeries
import time

# assigning var to the obtained API key
api_key = 'YOUR_API_KEY'

# set time series, key arguments and specify the output format as pandas df
ts = TimeSeries(key = api_key, output_format = 'pandas')
# set variables, pull data in varied values daily, weekly, pass in a ticker into symbol
# specify the time interval and output
data, meta_data = ts.get_intraday(symbol = 'ASX', interval= '1min', outputsize = 'full')
# print(data)

# Data Analysis
# Print volatility of stock in a last minute

# Step1: Get the closing data from pandas dataframe
close_data = data['4. close']
# print(close)

# step2 : Get the percent change of closing value in between each min
# pandas built in function called percent change is called
percent_change = close_data.pct_change()
# print(percent_change)

# pull out last value from the series
last_change = percent_change[-1]
# print(last_change)

# if absolute value of the last_change is above certain action do this
if abs(last_change) > 0.007:
    print("ASX Alert:" + last_change)
else:
    print("No change in last value")