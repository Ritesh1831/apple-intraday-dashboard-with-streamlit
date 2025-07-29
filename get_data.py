import requests
import pandas as pd

API_KEY = 'YOUR_API_KEY'   
# for api visit : https://www.alphavantage.co/ 
SYMBOL = 'AAPL'        
INTERVAL = '5min'          

# build url
url = (
    f'https://www.alphavantage.co/query?'
    f'function=TIME_SERIES_INTRADAY'
    f'&symbol={SYMBOL}'
    f'&interval={INTERVAL}'
    f'&outputsize=compact'
    f'&apikey={API_KEY}'
)


response = requests.get(url)
data = response.json()

 
time_series_key = f'Time Series ({INTERVAL})'
time_series = data.get(time_series_key, {})


df = pd.DataFrame.from_dict(time_series, orient='index')


df.rename(columns={
    '1. open': 'open',
    '2. high': 'high',
    '3. low': 'low',
    '4. close': 'close',
    '5. volume': 'volume'
}, inplace=True)


df.index = pd.to_datetime(df.index)


df = df.apply(pd.to_numeric)


df = df.sort_index()

df.to_csv(f'{SYMBOL}.csv')

print("✅ Data cleaned & saved to 'cleaned_intraday.csv'")