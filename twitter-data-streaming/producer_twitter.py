from decouple import config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092') #Same port as your Kafka server


topic_name = "twitter_data"


class twitterAuth():
    """SET UP TWITTER AUTHENTICATION"""

    def authenticateTwitterApp(self):
        access_token = config('ACCESS_TOKEN')
        access_token_secret = config('ACCESS_TOKEN_SECRET')
        consumer_key = config('API_KEY')
        consumer_secret = config('API_SECRET_KEYS')

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        return auth



class TwitterStreamer():

    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = twitterAuth()

    def stream_tweets(self):
        while True:
            listener = ListenerTS() 
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track=["Elections"], stall_warnings=True, languages= ["en"])


class ListenerTS(StreamListener):

    def on_data(self, raw_data):
            producer.send(topic_name, str.encode(raw_data))
            return True


if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()
