import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(murdered OR raped OR robbed (from:ANI OR from:AsianDigest) until:2022-06-09 since:2017-09-09"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
# print(df)

# to save to csv
df.to_csv('tweets.csv')