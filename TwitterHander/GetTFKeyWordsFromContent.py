#coding:utf-8
import os, sys, pprint
import nltk
# nltk.download()
import math
import string
import codecs
import csv
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter

# f = codecs.open('c:/intimate.txt','r','utf-8')
class TFMaker:

    def get_tokens(self,text):
        textLow = text.lower()
        tokens = WordPunctTokenizer().tokenize(textLow)
        words = [x for x in tokens if x not in string.punctuation and x not in ['."', '".', '?"', '!"', '%"', '%.']]
        return words

    def get_tokensForBigData(self,text):
        tokens = WordPunctTokenizer().tokenize(text)
        words = [x for x in tokens if x not in string.punctuation
                 and x not in ['.','."', '".', '?"', '!"', '%"', '%.','@']]
        return words

    def lemmatizer_tokens(self,tokens, lemmatizer):
        lemmatization = []
        for w in tokens:
            lemmatization.append(lemmatizer.lemmatize(w))
        return lemmatization


    def count_term(self,text):
        tokens = self.get_tokens(text)
        filtered = [w for w in tokens if w not in stopwords.words('english')]
        lemmatizer = WordNetLemmatizer()
        lemmatization = self.lemmatizer_tokens(filtered, lemmatizer)
        count = Counter(lemmatization)
        return count


    def tf(self,word, count):
        return count[word] / float(sum(count.values()))

    def csv2dict(self,file, key, value):
        IDFdict = {}
        with open(file, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            fieldnames = next(reader)
            reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
            for row in reader:
                IDFdict[row[key]] = row[value]
        return IDFdict

    def GetTFKeyWords(self,text, NumberOfTop=10):
        WordList_String = ''
        ScoreList_String = ''
        if text is not None:
            count = self.count_term(text)
            scores={}
            IDFdict = self.csv2dict(os.path.split(os.path.realpath(__file__))[0] + '/wordOccurrencesAlt.csv', 'Term', 'Document Frequency')
            for word in count:
                try:
                    IDFvalue = math.log(806791/(1.0 + float(IDFdict[word])))
                    scores[word] = self.tf(word, count) * IDFvalue
                except:
                    pass
            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            i = 0
            for word, score in sorted_words:
                WordList_String += word
                WordList_String += ','
                ScoreList_String += (str)(round(score, 5))
                ScoreList_String += ','
                i += 1
                if i == NumberOfTop:
                    return WordList_String, ScoreList_String

# tf=TFMaker()
# print(tf.GetTFKeyWords('this is first Articles to try our A tf-idf Maker, I hope it can work for this time bus cars cars please please',5))