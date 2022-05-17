import pandas as pd
import tweepy

def printtweetdata(n, ith_tweet):
	print()
	print(f"Tweet {n}:")
	print(f"Username:{ith_tweet[0]}")
	print(f"Description:{ith_tweet[1]}")
	print(f"Location:{ith_tweet[2]}")
	print(f"Tweet Text:{ith_tweet[3]}")
	print(f"Hashtags Used:{ith_tweet[4]}")
 
def scrape(words, date_since, numtweet):
    db = pd.DataFrame(columns=['username','description','location','text','hashtags'])
    tweets = tweepy.Cursor(api.search_tweets,words, geocode = "28.7041,77.1025,3000km",lang="en",since_id=date_since,tweet_mode='extended').items(numtweet)
    # tweets = tweepy.Paginator(client.search_recent_tweets, query=words,max_results=numtweet, limit=5)
    #tweets = client.search_recent_tweets(query=words, max_results=numtweet)

    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1
    print(list_tweets)
    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        hashtags = tweet.entities['hashtags']

            # Retweets can be distinguished by
            # a retweeted_status attribute,
            # in case it is an invalid reference,
            # except block will be executed
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [username, description,location, text, hashtext]
        db.loc[len(db)] = ith_tweet

        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i+1
    filename = 'scraped_tweets.csv'
    print("Hello")
    # we will save our database as a CSV file.
    db.to_csv(filename)


if __name__ == '__main__':

    consumer_key = 'sk2VuWW1kReEoY2qVFuq9lfG5'
    consumer_secret = 'D977Q3sK0vsYcWgUBIWjoRZHQ6GZvhv0ccFkcp0dz3m0PpgWf8'
    access_token = '1221011921668694017-u7MoUzb97U7xUPnLdcouckk1Jp3VNs'
    access_token_secret = 'oNdFPrBX1VYbXuGowuzmP3sXx9bzuFNhJC8kpWeW3FeER'

    #client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAO%2BaYQEAAAAAg%2B5WnyA9ESw9kKxedQdnI6jkxow%3Dnx6cfu1hw2clhkH6CwLZ1y2pByPNGVIwMClA4IvRoTBrXEIoSQ')
    #client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Enter Hashtag and initial date
    #print("Enter Twitter HashTag to search for")
    words = "crime"
    #print("Enter Date since The Tweets are required in yyyy-mm--dd")
    date_since = "2020-01-01"

    # number of tweets you want to extract in one run
    numtweet = 1000
    scrape(words, date_since, numtweet)
    print('Scraping has completed!')