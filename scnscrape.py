import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#snatching OR #gunpoint OR #threatened) -terrorists -Pakistan -Pakistani -BJP -Congress -AAP -party (from:timesofindia OR from:BBCIndia OR from:DDNewslive OR from:1stIndiaNews OR from:NewsArenaIndia) until:2022-06-09 since:2013-09-09"
# (kidnap OR theft OR burglary OR murder OR killed OR robbery OR rape OR raped OR stabbed
# 
tweets = []
limit = 20000


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