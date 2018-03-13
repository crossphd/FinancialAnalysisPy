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

# Add Returns column
# Method 1: Using shift
tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1) ) - 1
#print(tesla.head())

# Method 2: panda returns function
tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)

# # Plot histogram for each company
ford['returns'].hist(bins=50)
# plt.show()
gm['returns'].hist(bins=50)
# plt.show()
tesla['returns'].hist(bins=50)
# plt.show()

# Plot combined histogram
tesla['returns'].hist(bins=100,label='Tesla',figsize=(10,8),alpha=0.5)
gm['returns'].hist(bins=100,label='GM',alpha=0.5)
ford['returns'].hist(bins=100,label='Ford',alpha=0.5)
plt.legend()
# plt.show()

# Kernel Density graph
tesla['returns'].plot(kind='kde',label='Tesla',figsize=(12,6))
gm['returns'].plot(kind='kde',label='GM')
ford['returns'].plot(kind='kde',label='Ford')
plt.legend()
# plt.show()

# Box Plots
box_df = pd.concat([tesla['returns'],gm['returns'],ford['returns']],axis=1)
box_df.columns = ['Tesla Returns',' GM Returns','Ford Returns']
box_df.plot(kind='box',figsize=(8,11),colormap='jet')
# plt.show()

# Comparing Daily Returns between stocks
# Scatter Matrix
scatter_matrix(box_df,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50})
# plt.show()

# Scatter plot between just ford and gm
box_df.plot(kind='scatter',x=' GM Returns',y='Ford Returns',alpha=0.4,figsize=(10,8))
# plt.show()
