import tensorflow as tf
from sklearn.model_selection import train_test_split
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from flair.models import TextClassifier
from flair.data import Sentence

#Sentiment analysis
def sentiment_analysis(batch_size=1000, n_jobs=-1, n=300000):
    df = pd.read_csv('Final_Dataset.csv', encoding='utf-8', nrows=n)
    classifier = TextClassifier.load('en-sentiment')
    df['Sentiment'] = df['Tweets'].apply(lambda x: Sentence(x))
    df['Sentiment'] = df['Tweets'].apply(lambda x: classifier.predict(x))
    df['Sentiment'] = df['Sentiment'].apply(lambda x: x[0].labels[0].value)
    df.to_csv('Final_Dataset.csv',index=False)