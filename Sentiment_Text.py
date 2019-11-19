import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import sys

import pandas


df = pandas.read_csv('data.csv', encoding= 'ISO-8859-1')

print(df['comment_text'])
lines2 = df['comment_text']

sys.stdout=open("output.txt" , "w", encoding='ISO-8859-1')

sid = SentimentIntensityAnalyzer()
i = -1

for sentence in lines2:
     print( '     ' + i.__str__()  + '     ,'+ sentence )
     i=i+1
     ss = sid.polarity_scores(sentence)
     for k in ss:
        print( '{0}, {1}, '.format(k, ss[k]), end='')



