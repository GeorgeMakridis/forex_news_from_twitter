import pandas as pd
import time
import _0_configurations as conf
import sys
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')

news_df = pd.read_csv('input/'+str(conf.NEWS_ACOUNT)+'_polarity.csv')

price_df = pd.read_csv('input/EURUSD 1min_with_timestamp.csv')

news_df['publish_date_min']=news_df['publish_date'].values.astype('<M8[m]')
news_df['Timestamp']=news_df['publish_date_min'].values.astype(np.int64)//10**9
print (news_df.head())

#print(news_dataframe['publish_date_new_timpstamp'].duplicated().sum())

merged_dataframe=pd.merge(price_df, news_df, on='Timestamp', how='outer')
merged_dataframe = merged_dataframe[['Timestamp', 'close', 'polarity', 'cumsum']]

# merged_dataframe.fillna(method='ffill', inplace=True)

merged_dataframe.to_csv('input/dokimi.csv')

# merged_dataframe = merged_dataframe[merged_dataframe['Timestamp']<1410161838]

import matplotlib.pyplot as plt

x = merged_dataframe['Timestamp'].values
y = (merged_dataframe['cumsum'].values/30 )+1
z = merged_dataframe['close'].values

# w = np.correlate(z,y, "full")

plt.plot(x, y, 'b-', x,z,'r-')
plt.show()