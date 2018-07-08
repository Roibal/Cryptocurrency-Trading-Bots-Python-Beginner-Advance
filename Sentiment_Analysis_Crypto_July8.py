"""
Twitter Sentiment Analysis in Python - A bot which will monitor, store and categorize Sentiment Analysis based on Twitter
for cryptocurrencies, and implement a strategy for profitable trading based on Bitcoin Barbie Bot (BBB) Strategy, described here:

https://medium.com/@BlockchainEng/crypto-trading-bot-sentiment-analysis-bot-bfbd8dd1df5a

Youtube Series Here:
6/30/2018
source of BitcoinPrice() code: https://gist.github.com/mattvukas/9146611

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
import time
#textblob.download_corpora()
from datetime import datetime
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt
import requests, json
from time import sleep

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

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
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

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

    def tweet_file(self):
        self.message="Sentiment Analysis by @BlockchainEng"
        self.filename='SentimentAnalysis.png'
        print(self)
        self.api.update_with_media(message = self.message, filename= self.filename)

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
            list_of_tweets = []
            for tweet in fetched_tweets:

                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                #tweet1 =
                #tweet1=TwitterClient.api.clean_tweet(tweet_text)
                parsed_tweet['text'] = tweet.text
                list_of_tweets.append(tweet.text)
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
            with open('TweetHistory.txt', 'a+') as f1:
                for tweet in list_of_tweets:
                    try:
                        f1.write(tweet)
                    except:
                        pass

            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    search_term = 'Bitcoin'
    list_coins=['Bitcoin'] #, 'Ethereum', 'EOS', 'Cryptocurrency', 'Blockchain', 'BTC'] #'Donald Trump', 'Barack Obama', 'George Washington']
    count1=200
    list_coin_val = []
    start_time = datetime.now()
    try:
        for i in range(0,60):
            #This For Loop controls how many data 'cycles' are collected before visualization and tweeting
            for coin in list_coins:
                tweets = api.get_tweets(query = coin, count = count1)

                # picking positive tweets from tweets
                ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
                # percentage of positive tweets
                print("\n\nTime: {}".format(str(datetime.now())))
                print("Sentiment Values for {}\nNumber of Tweets Analyzed: {}".format(coin, count1))
                positive_tweet_percentage = round(100*len(ptweets)/len(tweets),6)
                print("Positive tweets percentage: {} %".format(positive_tweet_percentage))
                # picking negative tweets from tweets
                ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
                # percentage of negative tweets
                negative_tweet_percentage = round(100*len(ntweets)/len(tweets),6)
                print("Negative tweets percentage: {} %".format(negative_tweet_percentage))
                # percentage of neutral tweets
                neutral_tweet_percentage = round(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets),6)
                print("Neutral tweets percentage: {} % \
                    ".format(neutral_tweet_percentage))
                current_price = getBitcoinPrice()
                list_coin_val.append([coin, positive_tweet_percentage, negative_tweet_percentage, neutral_tweet_percentage, str(datetime.now()), current_price])
                save_to_file(coin, positive_tweet_percentage, negative_tweet_percentage, neutral_tweet_percentage, datetime.now(), current_price, "SentimentHistorical.csv")
                print("Current Price: {}".format(getBitcoinPrice()))
                trading(current_price, positive_tweet_percentage, negative_tweet_percentage)    #used for Trading Signals
            time.sleep(30)
        end_time = datetime.now()
        print(list_coin_val, start_time, end_time)
    except:
        print("ERROR - COLLECTING DATA")
    try:
        #msg = 'Sentiment Analysis - Twitter \nvia @BlockchainEngineer \n\n #cryptocurrency #bitcoin #bitcointrading'
        #filename = 'SentimentAnalysis.png'
        #api.tweet_file()
        data_visualize(api, list_coin_val, start_time, end_time)
        #historic_data_viz(api)
    except:
        print("ERROR - COLLECTING DATA")

def save_to_file(coin, positive_tweet_percentage, negative_tweet_percentage, neutral_tweet_percentage, time, current_price, filename = "SentimentHistorical.csv"):
    with open(filename, 'a+') as  f:
        line = coin, positive_tweet_percentage, negative_tweet_percentage, neutral_tweet_percentage, time, current_price
        f.writelines(str(line) + '\n')
def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

def tweet_file(self, message, filename):
    #message = "Sentiment Analysis by @BlockchainEng"
    #filename ='SentimentAnalysis.png'
    self.api.update_with_media(message, filename)

def historic_data_viz(self):
    #Load Historic Data and Visual into graph form for entire recorded amount
    historic_data_list = []
    i=0
    with open('SentimentHistorical.csv') as f1:
        lines = list(f1.readlines())
        for line in lines:
            print(line)
            data=list(line.split(','))
            print(data)
            if i==0:
                start_time=data[5]
            if i==len(f1.readlines()):
                end_time=data[5]
            historic_data_list.append(data)
            i+=1
    data_visualize(historic_data_list, start_time, end_time, self)

def trading(current_price, positive_sentiment_percent, negative_sentiment_percent):
    print("Positive Sentiment - Negative Sentiment (Net Positive)", positive_sentiment_percent-negative_sentiment_percent)
    if positive_sentiment_percent>0.3:
        #Buy
        #use Khal's Code to place order, entries & exits
        print("TEST - BUY SIGNAL")
        pass
    if negative_sentiment_percent>0.2:
        #Sell
        print("TEST - SELL SIGNAL")
        #use Khal's Code to place order, entries & exits
        pass

def data_visualize(api, list_coins, start_time, end_time):
    visualize_price = []
    name_list = []
    positive_tweet = []
    negative_tweet = []
    neutral_tweet = []
    time_list = []
    for coin in list_coins:
        print("COIN: ", coin)
        print(positive_tweet)
        print(coin[0])
        name_list.append(coin[0])
        positive_tweet.append(coin[1])
        print(coin[1])
        negative_tweet.append(coin[2])
        neutral_tweet.append(coin[3])
        time_list.append(coin[4])
        visualize_price.append(coin[5])
    #Converted to two axis on same graph - https://matplotlib.org/gallery/api/two_scales.html
    fig, ax1 = plt.subplots()

    color = 'black'
    ax1.set_xlabel('time')
    ax1.set_ylabel('Percentage', color=color)
    plt.title("Sentiment Analysis through Twitter \nCopyright 2018 (c) by @BlockchainEng")
    #ax1.plot(t, data1, color=color)
    ax1.plot(time_list, positive_tweet, 'g', label='Positive %')
    ax1.plot(time_list, negative_tweet, 'r', label='Negative %')
    ax1.plot(time_list, neutral_tweet, 'k', label = 'Neutral %')
    ax1.tick_params(axis='y', labelcolor=color)
    plt.legend()
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'blue'
    ax2.set_ylabel('Price ($)', color=color)  # we already handled the x-label with ax1
    #ax2.plot(t, data2, color=color)
    ax2.plot(time_list, visualize_price, 'b', label='Bitcoin Price (Bitstamp)')
    ax2.tick_params(axis='y', labelcolor=color)
    plt.legend()
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    """
    #print(positive_tweet)
    fig = plt.figure(1)
    plt.subplot(211)
    plt.plot(time_list, positive_tweet, 'g', label='Positive Tweet Percentage')
    plt.plot(time_list, negative_tweet, 'r', label='Negative Tweet Percentage')
    plt.plot(time_list, neutral_tweet, 'k', label = 'Neutral Tweet Percentage')
    plt.legend()
    plt.subplot(212)
    plt.plot(time_list, visualize_price, 'b', label='Bitcoin Price (Bitstamp)')
    plt.suptitle('{} Sentiment Analysis, 200 Tweets (each)\n{} - {} '.format(name_list[0], start_time, end_time))
    plt.legend()
    plt.ylabel('Percentage')
    plt.xlabel('Time')
    #plt.show()
    """
    plt.legend()
    #ax2.title('{} Sentiment Analysis, 200 Tweets (each)\n{} - {} '.format(name_list[0], start_time, end_time))
    filename='SentimentAnalysis.png' #+str(start_time).strip()+'.png'
    fig.savefig(filename)
    #tweet out fig and message
    msg = "@Twitter Sentiment Analysis for conversation around #Bitcoin - 200 tweets measured each cycle"
    msg+= "\n\n Includes price. \n\nvia @BlockchainEng \n\n #SentimentAnalysis #BitcoinTrading #Bitcoin"
    api.tweet_file()
    """
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
    """

if __name__ == "__main__":
    # calling main function
    while 1:
        main()
