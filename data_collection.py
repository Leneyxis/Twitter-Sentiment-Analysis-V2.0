import tweepy as tw
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()


# Twitter API credentials
ckey = os.getenv('api_key')
csecret = os.getenv('api_secret_key')
akey = os.getenv('access_token')
asecret = os.getenv('access_token_secret')

consumer_key = ckey
consumer_secret = csecret
access_token = akey
access_token_secret = asecret

# Authenticate to Twitter
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

# Collect Tweets and Create a Database
def tweets_collection(query):
    tweets=tw.Cursor(api.search_tweets,q=query, lang="en").items(50)
    data = [[tweet.text, tweet.created, tweet.user.screen_name] for tweet in tweets]
    return pd.DataFrame(data,columns=['tweet','date','username'])

def main():
    df = None
    query = ['Life', 'Freedom', 'Existence', 'Actions', 'Happiness', 'Consequences', 'Class Struggle', 'Caste', 'Capitalism', 'Exploitation'
             'Gender Equality', 'Patriarchy', 'Empowerment', 'Rights', 'Freedom', 'Democracy', 'Innovation', 'Representation', 'Traditions', 
             'Authority', 'Government', 'Individualism', 'Conservation', 'Bio-Diversity', 'Energy', 'Practicality', 'Sustainability',
             'Flexibility', 'Problem-Solving', 'Relativism','Discourse','Skepticism of metanarrative', 'Relativity', 'Grand Narratives', 'Focus']       
    for i in query:
        df = pd.concat([df, tweets_collection(i)])
    df.to_csv('data.csv')

main()