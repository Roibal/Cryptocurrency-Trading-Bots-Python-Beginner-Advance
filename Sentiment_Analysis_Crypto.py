"""
Twitter Sentiment Analysis in Python - A bot which will monitor, store and categorize Sentiment Analysis based on Twitter
for cryptocurrencies, and implement a strategy for profitable trading based on Bitcoin Barbie Bot (BBB) Strategy, described here:

https://medium.com/@BlockchainEng/crypto-trading-bot-sentiment-analysis-bot-bfbd8dd1df5a

Youtube Series Here:
6/30/2018

@BlockchainEng
Copyright 2018 - All Rights Reserved
"""

def run():
    #This Bot is to perform sentiment analysis, then implement a trade strategy based on sentiment and price
    """
    Monitor, collect and save tweets mentioning Cryptocurrency Y in file format.
    Perform Sentiment Analysis on a historic data set, and recent tweets during a specified time period (1 hour, 5 minutes, 1 day). Track and record historical values in file format. Visualize data through python script.
    Trade structure attempting to mimic this strategy:
    If Sentiment positive (‘buy’) and green candle (‘higher price’), wait to purchase coins.
    If candle decreases 2% (or more) in specified time period (5 minutes, 1 hour, 1 day), Purchase quantity of coin.
    Sell when price increases 5% (adjustable).
    To Reiterate, the functionality of of a bot to implement this strategy is based on a python script that will:

    Monitor all tweets mentioning X-Coin, perform sentiment analysis to determine buy/sell signalling from crypto-accounts
    Track Historical Values in CSV spreadsheet format
    Compare current/recent values to historic values
    Tweet out ‘Alerts’ based on strategy, and perform successful trades on Binance

    :return:
    """
    #Instructions: https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
import tweepy
import textblob

textblob.download_corpora

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
        consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])
                                    |(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = 'Donald Trump', count = 200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % \
        ".format(100*len(tweets - ntweets - ptweets)/len(tweets)))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])

if __name__ == "__main__":
    # calling main function
    main()
