import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pandas_datareader
import pandas_datareader.data as web
import datetime
from pandas.plotting import scatter_matrix

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)

tesla = web.DataReader("TSLA", 'yahoo', start, end)
ford = web.DataReader("F", 'yahoo', start, end)
gm = web.DataReader("GM", 'yahoo', start, end)

# Add daily returns column (from dailyreturns.py)
tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)

# Create a cumulative daily return column for each car company's dataframe.
tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()
ford['Cumulative Return'] = (1 + ford['returns']).cumprod()
gm['Cumulative Return'] = (1 + gm['returns']).cumprod()

print(tesla.head())

# Now plot the Cumulative Return columns against the time series index.
# Which stock showed the highest return for a $1 invested? Which showed the lowest?
tesla['Cumulative Return'].plot(label='Tesla',figsize=(16,8),title='Cumulative Return')
ford['Cumulative Return'].plot(label='Ford')
gm['Cumulative Return'].plot(label='GM')
plt.legend()
plt.show()


