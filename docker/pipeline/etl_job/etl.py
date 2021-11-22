
import pymongo
from sqlalchemy import create_engine
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

time.sleep(10)  # seconds

client = pymongo.MongoClient("mongodb")
db = client.tweets

pg = create_engine('postgresql://dummy:1234@postgresdb:5432/tweets', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

entries = db.collections.tweets.find()
for e in entries:
    print(e)
    text = e['text']
    sentiment = s.polarity_scores(text)
    print(sentiment)

    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))
