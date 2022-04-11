import pyupbit
crypto_list = pyupbit.get_tickers(fiat='KRW')
current_price = pyupbit.get_current_price(["KRW-BTC","KRW-ETH"])

# previous data

ticker = 'KRW-BTC'
interval = 'minute1'
to = '2022-02-01 00:01'
count = 4000000
df = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)
df.to_csv('./bitcoin_minute1.csv')
print(df)
