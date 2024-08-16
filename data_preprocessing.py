import pandas as pd
import re
import os

#Read and combine the Dataset.
def combine_datasets()->'csv': # type: ignore
    df = pd.read_csv('Dataset1.csv', encoding='utf-8') 
    statements=df['comment'].to_list()
    df = pd.DataFrame(statements,columns=['Tweets'])
    df.to_csv('Final_Dataset.csv')


#Preprocess the Dataset. Remove url, mentions, and hashtags.
def preprocessing()->'csv': # type: ignore
    df = pd.read_csv('Final_Dataset.csv', encoding='utf-8')
    df['Tweets'] = df['Tweets'].astype(str)
    df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"http\S+|@\S+|#\S+", "", x))
    df=df.dropna()
    df.to_csv('Final_Dataset.csv',index=False)


def main():
    if os.path.isfile('Final_Dataset.csv') == False:
        combine_datasets()
        preprocessing()
    return("Preprocessing Done")

main()