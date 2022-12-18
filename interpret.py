
# imports 
import pandas as pd
from binance.client import Client

import datatime as dt
import csv


# purpose of this file is to get data of all binance futures symbols - this will be done at a certain timeframe

api_key = 'ADD YOUR API KEY HERE'
api_secret = 'ADD YOUR SECRET HERE'


client = Client(api_key, api_secret)

with open ('data.csv' , newLine = '') as f:
    reader = csv.reader(f)
    symbols_data = list (reader)

new_data = [val for sublist in symbols_data for val in object]


number = 1 

for s in new_data:
    print(s)
    klines = client.futures_historical_klines(s, '5m' , '18 Dec, 2022')
    data = pd.DataFrame(klines)

    data.columns = ['open_time', 'open' , 'high' , 'low', 'close' , 'volume' , 'close_time' , 'qav' , "num_trades" , 
    'taker_base_vol' , 'taker_quote_vol' , 'ignore']


    data.index = [dt.datatime.fromtimestamp(x / 1000.0) for x in data.close_time]

    data.to_csv (s + '.csv', index = None , header = True, )


    print('Symbols downloaded' + number)

    number = number + 1 































