from __future__ import print_function
import tweepy
import pandas as pd
import preprocessor as p
import time
import _0_configurations as conf

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def parse_tweets(tweets):
    times = []
    text = []

    for status in tweets.items():
        # print (status._json['text'])
        tweet_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                   time.strptime(status._json['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        # tweet_time = time.strftime('%Y-%m-%d',
        #                            time.strptime(status._json['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        times.append(tweet_time)
        tweet_text = status._json['text'].encode('utf-8')
        text.append(tweet_text)

    return times, text


def clean_tweets(tweet):
    # p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.HASHTAG)
    return p.clean(tweet).encode('utf-8')



# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(conf.CONSUMER_KEY, conf.CONSUMER_SECRET)
auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.user_timeline, screen_name=conf.NEWS_ACOUNT)

times,text = parse_tweets(tweets)


dataframe = pd.DataFrame(times, columns=['publish_date'])
dataframe['text'] = text

dataframe['headline_text'] = map(clean_tweets, dataframe['text'])

print(dataframe.shape)
dataframe.drop(['text'], axis=1, inplace=True)

dataframe.dropna(inplace=True)
print(dataframe.shape)

dataframe.to_csv('input/'+str(conf.NEWS_ACOUNT)+'.csv', index=False)