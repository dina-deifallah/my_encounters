'''
1. EXTRACT the tweets from mongodb
- connect to the database 
- query the data

2. TRANSFORM the data
- clean the text before?
- sentiment analysis
- maybe transform data types?

3. LOAD the data into postgres
- connect to postgres 
- insert into postgres

'''
import time
from pymongo import MongoClient
from sqlalchemy import create_engine
import psycopg2

import ... 

### create connections to databases (check your mongosb and postgres in python notebooks (or luftdaten))

.. 

## Great suggestion: work step by step in each function with a limited amount of data e.g. 5 tweets, hence the .find(limit = 5) to test

def extract():
    ''' Extracts tweets from mongodb'''
    # how often?
    # only new ones?
    # always take all and deal with duplicates in the transform?
    # .find(limit = 5) and ADVANCED: if you want to filter .find({condition})
    # e.g. extracted_tweets is a list of dictionaries
    extracted_tweets = list(tweets.find(limit = 5))

    return exctracted_tweets

def transform(exctracted_tweets):
    ''' Transforms data: clean text, gets sentiment analysis from text, formats date '''
    ## sentiment analysis tomorrow, basically you pass text and get a number between 0-1 as the sentiment score
    ## add the sentiment to the tweet and store in a dataframe or a dictionary
    transformed_tweets = []
    for tweet in extracted_tweets:
        # some text clean up
        sentiment = 1 # later on you will calculate a sentiment
        # datatype of the tweet: dictionary
        tweet['sentiment'] = sentiment # adding a key: value pair with 'sentiment' as the key and the score as the value
        transformed_tweets.append(tweet)
        # transformed_tweets is a list of transformed dictionaries

    return transformed_tweets


def load(transformed_tweets):
    ''' Load final data into postgres'''
    ## example function to load
    for tweet in transformed_tweets:
        insert_query = "INSERT INTO tweets VALUES (%s, %s, %s)"
        db_pg.execute(insert_query, (tweet['user_name'], tweet['text'], tweet['sentiment']))
        logging.critical('---Inserted a new tweet into postgres---')
        logging.critical(tweet)


if __name__== "__main__":
    ### example: run ETL job every 2 minutes
    while True:
        extracted_tweets = extract()
        transformed_tweets = transform(extracted_tweets)
        load(transformed_tweets)
        time.sleep(120)

    