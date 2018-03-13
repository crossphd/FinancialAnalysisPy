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

print(tesla.head())

###
# plot opening prices
###
tesla['Open'].plot(label="Tesla", figsize=(14,8), title="Opening Prices")
gm['Open'].plot(label="GM")
ford['Open'].plot(label="Ford")
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.legend()
plt.show()


###
# plot trading volume
####
tesla['Volume'].plot(label="Tesla", figsize=(14,8), title="Volume Traded")
gm['Volume'].plot(label="GM")
ford['Volume'].plot(label="Ford")
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.legend()
plt.show()

print(ford['Volume'].argmax())

###
# create new total traded column and plot
###
tesla['Total Traded'] = tesla['Open']*tesla['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']
ford['Total Traded'] = ford['Open']*ford['Volume']

tesla['Total Traded'].plot(label='Tesla', figsize=(16,8), title="Total Traded")
gm['Total Traded'].plot(label='GM', figsize=(16,8), title="Total Traded")
ford['Total Traded'].plot(label='Ford', figsize=(16,8), title="Total Traded")
plt.legend()
plt.show()


###
# plot moving averages
###
gm['MA 50'] = gm['Open'].rolling(50).mean()
gm['MA 200'] = gm['Open'].rolling(200).mean()
gm[['Open','MA 50','MA 200']].plot(title="Moving Averages", figsize=(16,8))
plt.legend()
plt.show()


###
# scatter matrix plot to check relationship between opening prices
###
car_comp = pd.concat([tesla['Open'], gm['Open'],ford['Open']],axis=1)
car_comp.columns = ['Tesla Open','GM Open','Ford Open']

print(car_comp.head())

scatter_matrix(car_comp, figsize=(8,8),alpha=0.2,hist_kwds={'bins':50});
plt.show()


###
# CandleStick chart for Ford in January 2012
###
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY

# Rest the index to get a column of January Dates
ford_reset = ford.loc['2012-01':'2012-01'].reset_index()

# Create a new column of numerical "date" values for matplotlib to use
ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))
ford_values = [tuple(vals) for vals in ford_reset[['date_ax', 'Open', 'High', 'Low', 'Close']].values]

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#Plot it
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values, width=0.6, colorup='g',colordown='r')
plt.show()