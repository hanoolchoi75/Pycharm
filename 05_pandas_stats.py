import pandas as pd
from pandas_datareader import data

all_data = {}

for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = data.DataReader(ticker, 'yahoo', '2015-01-01', '2016-01-01')

price = pd.DataFrame({tic:data['Adj Close'] for tic, data in all_data.items()})
volume = pd.DataFrame({tic:data['Volume'] for tic, data in all_data.items()})

returns = price.pct_change()
# print(type(returns))
# print(returns.tail())
print(returns.MSFT.corr(returns.IBM))
print(returns.MSFT.cov(returns.IBM))
print(returns.corr())
print(returns.cov())
print(returns.corrwith(returns.IBM))
print(returns.corrwith(volume))
# print(returns.corrwith(volume, axis=1)) 책에서 하라고는 했는데 왜 하는지 모르겠다.
