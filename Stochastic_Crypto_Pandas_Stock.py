"""

The purpose of this software is to format Bitcoin Price and DJIA into a Pandas format
which will then be analyzed using Stochastic methods with TA-Lib

Created 12/26/2018

Inspired by Sentdex "Pandas" tutorial

Copyright 2018 by Joaquin Roibal (@BlockchainEng)

"""

import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
#import talib as ta
import numpy as np

style.use('ggplot')

#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2015, 1, 1)
def run():
    #Format 30 Day Historical Data from CoinMarketCap into a Pandas data format
    url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20180727&end=20181227'
    btc90day = pd.read_html(url, header=0)
    btc_30_sma = simple_moving_average(btc90day[0]['Close**'])
    #btc_30_sma += btc90day[0]['Close**'][0:29]
    print(btc_30_sma)
    print(btc90day[0].head())
    plt.figure(1)
    #plt.subplot(121)
    ax = plt.gca()
    plt.plot(btc90day[0]['Date'], btc90day[0]['Close**'], label='Bitcoin', color='Black')
    plt.plot(btc90day[0]['Date'][:-29], btc_30_sma, label='30 Day BTC SMA', color = 'Red') #Graph 30 day MA, format due to no values for 29 days
    plt.title("Bitcoin 6 Month Price at Close\nCopyright 2019 by Joaquin Roibal")
    #btc30day[0]['Close**'].plot()
    ax.invert_xaxis()
    #plt.plot(btc90day[0]['Date'], btc_30_sma, label='30 day SMA')
    plt.legend()
    #plt.show()
    #plt.subplot(122)
    #Format Historical Dow Jones Industrial Average into a Pandas format
    plt.figure(2)
    url2 = "https://finance.yahoo.com/quote/%5EDJI/history/"
    DJIA = pd.read_html(url2, header=0)
    DJIA[0]=DJIA[0][:-1]
    print(DJIA[0])
    DJIA_30_sma = simple_moving_average(DJIA[0]['Close*'])
    ax = plt.gca()
    plt.title("Dow Jones 90 Day Price at Close\nCopyright 2019 by Joaquin Roibal")
    plt.plot(DJIA[0]['Date'], DJIA[0]['Close*'], label='DJIA', color = 'Black')
    plt.plot(DJIA[0]['Date'][:-29], DJIA_30_sma, label='DJIA 30 Day SMA', color = 'Red') #Graph 30 day MA, format due to no values for 29 days
    ax.invert_xaxis()
    #plt.yscale('log')
    plt.legend()
    plt.show()

    #create 5 year, logarithmic btc data visualization

    urlalltime = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20131227&end=20181227"
    btcalltime = pd.read_html(urlalltime, header = 0)
    print(btcalltime[0].head())
    #btcalltime[0]['Close**'].plot()
    #plt.plot(btcalltime[0]['Date'], btcalltime[0]['Close**'])
    #plt.show()

# Following Code from: https://stackoverflow.com/questions/30261541/slow-stochastic-implementation-in-python-pandas

def simple_moving_average(prices, period=30):
    """
    :param df: pandas dataframe object
    :param period: periods for calculating SMA
    :return: a pandas series
    """
    weights = np.repeat(1.0, period)/period
    sma = np.convolve(prices, weights, 'valid')
    return sma


def fast_stochastic(lowp, highp, closep, period=14, smoothing=3):
    """ calculate slow stochastic
    Fast stochastic calculation
    %K = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100
    %D = 3-day SMA of %K
    """
    low_min = pd.rolling_min(lowp, period)
    high_max = pd.rolling_max(highp, period)
    k_fast = 100 * (closep - low_min)/(high_max - low_min)
    k_fast = k_fast.dropna()
    d_fast = simple_moving_average(k_fast, smoothing)
    return k_fast, d_fast


def slow_stochastic(lowp, highp, closep, period=14, smoothing=3):
    """ calculate slow stochastic
    Slow stochastic calculation
    %K = %D of fast stochastic
    %D = 3-day SMA of %K
    """
    k_fast, d_fast = fast_stochastic(lowp, highp, closep, period=period, smoothing=smoothing)

    # D in fast stochastic is K in slow stochastic
    k_slow = d_fast
    d_slow = simple_moving_average(k_slow, smoothing)
    return k_slow, d_slow

if __name__ == "__main__":
    run()