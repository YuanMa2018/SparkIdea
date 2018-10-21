# coding:utf-8
from TwitterHander.GetTFKeyWordsFromContent import TFMaker
from nltk.corpus import stopwords
import datetime
import re
from twython import TwythonStreamer


class WriteText:
    CountInstance=0
    MaxInstance = 1000
    def writeText(self,word_line):
        self.CountInstance = self.CountInstance + 1
        if(self.CountInstance/self.MaxInstance < 1):
            with open('weblog-flume.log', 'a') as f:
                f.write(" ".join(word_line)+'\n')
        else:
            self.CountInstance = 0
            with open('weblog-flume.log', 'w') as f:
                f.write(" ".join(word_line)+'\n')

class MyStreamer(TwythonStreamer):
    WordPreprocessor = TFMaker()
    WriteTextOBJ = WriteText()
    def on_success(self, data):
        if 'text' in data:
            publish_date = datetime.datetime.now()
            try:
                print(publish_date)
                OriginalData = data['text']
                print("Collecting---Original Sentence:   "+OriginalData)
                try:
                    link = re.search("(?P<url>https?://[^\s]+)", OriginalData).group("url")
                    OriginalData = OriginalData.replace(link, "")
                except:
                    pass
                tokens = self.WordPreprocessor.get_tokensForBigData(OriginalData)
                FilteredWords = [w for w in tokens if w.lower() not in stopwords.words('english') and 3 <= len(w)]
                word_line = FilteredWords[2:]
                if(word_line != None):

                    print("Collecting---After Clean:         " + " ".join(word_line))
                    self.WriteTextOBJ.writeText(FilteredWords[2:])
            except:
                pass

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




