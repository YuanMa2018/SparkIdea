# coding:utf-8
from TwitterHander.GetTFKeyWordsFromContent import TFMaker
from nltk.corpus import stopwords
import datetime
import re
from twython import TwythonStreamer



class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print('========================>')
        print(status_code)




def StartMonitor(KeyWord, NewsSource):
    ms = MyStreamer(app_key="keI3Ao8sAyC93ALONPlTUDxvN",
                    app_secret="rVDCnuOmaV3hCJzxyW0ywIc0GC9WldNSjaarMloXihOb8s2y7M",
                    oauth_token="932145228240375808-b7Fd1tHA47TLMJCn2YtwAkcgB7rzNlR",
                    oauth_token_secret="UMfRldTG6zhKlbHtEgE4I32rkXaFCLUf7UueB7ZOSlcD3")

    print("Key Word : ",KeyWord)
    print("News Source : ",NewsSource)
    ms.statuses.filter(
        track=[KeyWord],
        follow=[
        # The top 10 mainstream media sources are:
        788524,             # GuardianNews -
        612473,             # BBC -
        16343974,           # The Telegraph -
        1652541,            # Reuters Top News -
        807095,             # The New York Times -
        7587032,            # Sky News  -
        2467791,            # Washington Post -
        205770556,          #i newspaper -
        1367531,            #Fox News  -
        6107422,            #The Times of London -
        # The top 10 tabloid media sources are:
        16887175,           #  Mirror -
        17895820,           # Daily Express -
        380285402,          # Daily Mail US -
        34655603,           # The Sun -
        5695632,            # BuzzFeed -
        2969760609,         # POLITICO Europe -
        2887077099,         # The National -
        20442930,           #Daily Star  -
        474055087,          #The Evening Times -
        14224443,           #Plymouth Herald -
        # The top 10 alternative media sources are:
        38400130,           # Channel NewsAsia -
        18856867,           # zerohedge -
        64643056,           # RT -
        457984599,          # Breitbart News  -
        4081106480,         # The Daily Wire -
        143145579,          # The Poke -
        141422795,          #100% FED UP! -
        2768501,            #ABC News -
        21185021,           #NewsThump  -
        3957294317         #NewsTarget  -
    ])




StartMonitor("Xi","")