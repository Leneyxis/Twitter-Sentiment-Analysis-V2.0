import pandas as pd
import re
import os
import matplotlib.pyplot as plt


#Read and combine the Dataset.
def combine_datasets()->'csv': # type: ignore
    df = pd.read_csv('Dataset1.csv', encoding='utf-8') 
    statements=df['comment'].to_list()
    df = pd.read_csv('Twitter_Data.csv', encoding='utf-8')
    statements.extend(df['clean_text'].to_list())
    df = pd.read_csv('Reddit_Data.csv', encoding='utf-8')
    statements.extend(df['clean_comment'].to_list())
    df = pd.DataFrame(statements,columns=['Tweets'])
    df.to_csv('Final_Dataset.csv')

def main():
    if os.path.isfile('Final_Dataset.csv') == False:
        combine_datasets()

main()