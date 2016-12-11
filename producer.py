import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = 'xaaAErGrUEHURJNSrK0y2U4Lw'
consumer_secret = 'M35WlGRqkkW4ThmP7ax6e4YhlK4kd1vaY0nI0piJv3lCDgSO79'
access_token = '1035956736-NONVN9QwEcnUdUfoCVx1dX7GiOuxYrf6ILXfw7d'
access_secret = 'oCpeAL5ch5uRlTjOSah8Xz5reiDsY1lRgAIfd2Q6tQlNI'

def producer_say_hello():
    print("Hello World, from Producer")

class TPSOpsStreamListener(StreamListener):

    def on_data(self, data):
        send_msg(data)
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
        # 3108351 463933187
        tps_streaming.filter(follow=['3108351'], async=True)
    except:
        print("error") # print exception
        tps_streaming.disconnect()

def send_msg(message):
    print("producer")
    print(message)
