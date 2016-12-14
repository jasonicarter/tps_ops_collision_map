import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from pykafka import KafkaClient

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

class TPSOpsStreamListener(StreamListener):

    def on_data(self, data):
        send_tweets(data)
        return True

    # def on_status(self, status):
    #         send_msg(status)

    def on_error(self, status_code):
        if status_code == 420:
            print("Rate limited")
            return False

def start_stream():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    print("Stream starting...")
    tps_streaming = Stream(auth, TPSOpsStreamListener())

    try:
        # 3108351 463933187 (wsj and tps_ops)
        tps_streaming.filter(follow=['3108351'], async=True)
    except:
        print("error") # print exception
        tps_streaming.disconnect()

def producer_say_hello():
    print("Hello World, from Producer")

def producer_init(ip_address, topic):
    # TODO: set 9092 as default and add to ip_address
    client = KafkaClient(ip_address + ":9092")
    topic = client.topics[topic]

def produce_msg(*message):
    with topic.get_producer() as producer: # topic.get_producer(sync=True)
        if not message:
            for i in range(4): # while not your_app.needs_stopping:
                test_message = "test message " + str(i ** 2)
                producer.produce(test_message)
                print(test_message)
        else:
            producer.produce(message)
