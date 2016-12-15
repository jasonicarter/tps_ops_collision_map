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

    def on_status(self, status):
        client = KafkaClient(hosts="172.17.0.3" + ":9092")
        topic = client.topics[str.encode("test1")]

        with topic.get_producer() as producer:
            tweet_text = status.text
            producer.produce(str.encode(tweet_text))

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

def produce_msg(ip_address, k_topic, *message):
    # TODO: set 9092 as default and add to ip_address
    client = KafkaClient(hosts=ip_address)
    topic = client.topics[str.encode(k_topic)]

    with topic.get_producer() as producer: # topic.get_producer(sync=True)
        if not message:
            for i in range(400): # while not your_app.needs_stopping:
                test_message = 'test message ' + str(i ** 2)
                producer.produce(str.encode(test_message))
        else:
            producer.produce(message)
