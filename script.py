#!/usr/bin/env python

from datetime import datetime

from pattern.en import sentiment
from twitter import *


consumer_key = 'rvlDscXxbBgzIoOTDyekQ'
consumer_secret = '5pBwUvkvdAel3vNRAr7aGmOHJgcRvkOgdQG4gTvmDI'
access_token = '18888797-xOop1TynMBdW3u42XPFp1HmDwlHmnRrkkstlKAGIr'
access_secret = 'pJWAnf6w2zZ5NlNz2MKhXtOmFZM7ee8lVFIAAoTKtg'

#t = Twitter(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))
#btc = t.search.tweets(q='#bitcoin')

ts = TwitterStream(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))
btc_stream = ts.statuses.filter(track='#bitcoin')

polarity = []
subjectivity = []

def return_polarity_statement(polarity):
    statement = ''
    
    avg_polarity = sum(polarity) / float(len(polarity))

    if avg_polarity > 0:
        statement = 'bearish'
    elif avg_polarity < 0:
        statement = 'bullish'

    return statement

def return_subjectivity_statement(subjectivity):
    statement = ''
    
    avg_subjectivity = sum(subjectivity) / float(len(subjectivity))

    if avg_subjectivity > 0.5:
        statement = 'pontificating'
    elif avg_subjectivity < 0.5:
        statement = 'reporting objectively'

    return statement 

for tweet in btc_stream:
    s = sentiment(tweet['text'])
    polarity.append(s[0])
    subjectivity.append(s[1])
    
    #print '%s' % tweet['text']
    p = return_polarity_statement(polarity)
    s = return_subjectivity_statement(subjectivity)
    
    print 'As of %s, the Twittersphere is %s and %s about bitcoins' % (datetime.now(), p, s)

