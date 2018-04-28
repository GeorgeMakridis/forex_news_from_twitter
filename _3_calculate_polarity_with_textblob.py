import pandas as pd
from textblob import TextBlob
import sys
import _0_configurations as conf
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')


def text_blob_testimonal_polarity(tweet):
    testimonial = TextBlob(str(tweet))
    return testimonial.sentiment.polarity

def negative_news_multiply(polarity):
    if polarity<0:
        polarity = polarity
    return polarity

data = pd.read_csv('input/'+str(conf.NEWS_ACOUNT)+'_'+str(conf.ASSET)+'.csv')


data['polarity'] = map(text_blob_testimonal_polarity, data['headline_text'])

# data['polarity'] = map(negative_news_multiply, data['polarity'])


data = data.reindex(index=data.index[::-1])

data['publish_date'] = pd.to_datetime(data['publish_date'])

data['Timestamp'] = data.publish_date.values.astype(np.int64) // 10 ** 9

data['cumsum'] = data['polarity'].cumsum()

data.to_csv('input/'+str(conf.NEWS_ACOUNT)+'_polarity.csv', index=False)

import matplotlib.pyplot as plt

x = pd.to_datetime(data['publish_date'].values)
y = data['cumsum'].values

plt.plot(x,y)
plt.show()
