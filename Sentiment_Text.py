import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv


text_file = open('data.txt',  encoding='utf-8')
lines = text_file.read().splitlines()
print (lines)


sid = SentimentIntensityAnalyzer()
for sentence in lines:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
          print('{0}: {1}, '.format(k, ss[k]), end='')

































