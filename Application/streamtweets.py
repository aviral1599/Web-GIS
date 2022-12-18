import tweepy
import json
import time
import json
import random


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
# import twitter_credentials
 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler('sk2VuWW1kReEoY2qVFuq9lfG5', 'D977Q3sK0vsYcWgUBIWjoRZHQ6GZvhv0ccFkcp0dz3m0PpgWf8')
        auth.set_access_token('1221011921668694017-u7MoUzb97U7xUPnLdcouckk1Jp3VNs', 'oNdFPrBX1VYbXuGowuzmP3sXx9bzuFNhJC8kpWeW3FeER')
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list,locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078])


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.counter=0

    def on_data(self, data):
        try:
            data = json.loads(data)
            print(data)
            with open(self.fetched_tweets_filename, 'a+', encoding="utf-8") as tf:
                text = data["text"]
                print(type(text))
                print(text)
                tf.write(text)
            return True
                # def on_data(self,raw_data):
            # self.counter+=1
            # if(self.counter==11):
            #     return False
            # print_data(json.loads(data) )
            # return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)
        
def print_data(data):
        tweet_text=data['text'].encode('utf-8') if 'text' in data.keys() else None
        created_at=data['created_at'] if 'created_at' in data.keys() else None
        tweet_reply_count=data['reply_count'] if 'reply_count' in data.keys() else None
        user_screename=data['user']['screen_name']if 'screen_name' in data['user'].keys() else None
        user_location=data['user']['location'] if 'location' in data['user'].keys() else None
        # user_friends_count=data['user']['friends_count'] if 'friends_count' in data['user'].keys() else None
        # user_follower_count=data['user']['followers_count'] if 'followers_count' in data['user'].keys() else None     
        print("------------------------------------------------------------------------")
        print(f"Tweet Text : {tweet_text}:")
        print(f"Tweeted  At :{created_at}") 
        print(f"Username :{user_screename}")
        print(f"Location :{user_location}")
        # print(f"User friends count {user_friends_count}")
        # print(f"User Follower Count:{user_follower_count}")

 
def stream():
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ['murder','kidnap','theft','rape']
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)