#coding:utf-8
from twython import Twython, TwythonError, TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['user']['id'])
            print(data['text'])

    def on_error(self, status_code, data):
        print('========================>')
        print(status_code)







