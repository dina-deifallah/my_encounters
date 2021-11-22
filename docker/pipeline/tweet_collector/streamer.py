import tweepy
import config


class Listener(tweepy.StreamListener):

    def on_data(self, raw_data):

        self.process_data(raw_data)
        return True
    
    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            return False

class Stream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)

if __name__ == "__main__":
    listener = Listener()

    auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    stream.start(['Joe biden', 'donald trump'])