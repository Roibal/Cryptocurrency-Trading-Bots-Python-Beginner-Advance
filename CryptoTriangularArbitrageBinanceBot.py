"""
The Purpose of the Binance Arbitrage Bot (based on RoibalBot) Python Program is to create an automated trading bot (functionality) on Binance
Utilized Python-Binance ( https://github.com/sammchardy/python-binance )
Advanced-Version capable of all exchanges, all coins (using cctx)

Created 4/14/2018 by Joaquin Roibal
V 0.01 - Updated 4/20/2018
v 0.02 - Updated 5/30/2018 - Converted to Advanced Version: https://github.com/Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance
v 0.03 - Created 6/18/2018 - Binance Arbitrage Bot
v 0.04 - 6/21/2018 - Changed Name to CryptoTriangularArbitrageBinanceBot.py
Licensed under MIT License

Instructional Youtube Video: https://www.youtube.com/watch?v=8AAN03M8QhA

Did you enjoy the functionality of this bot? Tips always appreciated.

BTC:
ETH:

NOTE: All Subsequent Version of Program must contain this message, unmodified, in it's entirety
Copyright (c) 2018 by Joaquin Roibal
"""

from binance.client import Client
import time
from datetime import datetime
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
#import save_historical_data_Roibal
from BinanceKeys import BinanceKey1

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)

def run():
    #Initialize Arbitrage Binance Bot
    initialize_arb()
    #Get Binance Wallet Balance

    #Perform our Arbitrage Function
    #Data Output (log) in a text file - keep track of start/end time, trades, balance
    pass

def initialize_arb():

    print("\n\n---------------------------------------------------------\n\n")
    print("Hello and Welcome to the Binance Arbitrage Crypto Trader Bot Python Script\nCreated 2018 by Joaquin Roibal (@BlockchainEng)")
    print("A quick 'run-through' will be performed to introduce you to the functionality of this bot")
    print("To learn more visit medium.com/@BlockchainEng or watch introductory Youtube Videos")
    bot_start_time = str(datetime.now())
    print("Bot Start Time: {}".format(bot_start_time))
    time.sleep(5)
    try:
        status = client.get_system_status()
        #print("\nExchange Status: ", status)

        #Account Withdrawal History Info
        withdraws = client.get_withdraw_history()
        #print("\nClient Withdraw History: ", withdraws)

        #for symbol in list_of_symbols:
            #market_depth(symbol)
        #Collect all Symbols for Exchange
        #Find Arbitrage Opportunities
        list_of_symbols = ['ETHBTC', 'BNBETH', 'BNBBTC']
        list_of_symbols2 = ['ETHUSDT', 'BNBETH', 'BNBUSDT']
        list_of_symbols3 = ['BTCUSDT', 'BNBBTC', 'BNBUSDT']
        list_of_arb_sym = [list_of_symbols, list_of_symbols2, list_of_symbols3]
        #for sym in list_of_symbols:
            #info = client.get_symbol_info(sym)
            #print(info)
        #prices = client.get_all_tickers()
        tickers = client.get_orderbook_tickers()
        #print(prices)
        #print(tickers)
        #Run Arbitrage Profit Functionality - To Determine Highest Profit Percentage - Cont Loop
        while 1:
            calc_profit_list =[]
            for arb_market in list_of_arb_sym:
                calc_profit_list.append(arbitrage_bin(arb_market, tickers, 1, 1))
            print(calc_profit_list)
            exp_profit = 0      #Expected Profit, Set to 0 initially
            m = n = 0       #Market Position Market
            for exch_market in calc_profit_list:
                if exch_market[4]>exp_profit:
                    exp_profit = exch_market[4]
                    m = n
                n+=1
            print("\nMost Profitable Market: {} \nExpected Profit: {}%".format(list_of_arb_sym[m], exp_profit))
            time.sleep(20)
            #Run Arbitrage Function on Highest Profit Percentage Coin for 10 minutes
            arb_list_data = []
            arb_start_time = str(datetime.now())
            for i in range(0,5):
                #Collect Arbitrage Data Into List format for 5 cycles, 30 second cycles (replaces functionality)
                arb_list_data.append(arbitrage_bin(list_of_arb_sym[m], tickers, 1, 1))
                #print(arb_list_data)
                time.sleep(30)
            arb_end_time = str(datetime.now())
            #Visualize Collected Arb List Data with MatPlotLib
            viz_arb_data(arb_list_data, list_of_arb_sym[m], arb_start_time, arb_end_time)
    except:
        print("\nFAILURE INITIALIZE\n")

def arbitrage_bin(list_of_sym, tickers, cycle_num=10, cycle_time=30):
    #Create Triangular Arbitrage Function
    print("Binance Arbitrage Function Running")
    time.sleep(2)
    fee_percentage = 0.0005          #divided by 100
    #Created Arbitrage Functionality for  with Python-Binance
    for i in range(0,1):    #initialize Exchange
        #create blacklist of exchanges

            #exchange1 = getattr (ccxt, exch) ()
        #symbols = tickers.keys()
        #print(symbols)
        #time.sleep(20)
            #Find Pairs to Trade
        """
            pairs = []
            for sym in symbols:
                for symbol in coins:
                    if symbol in sym:
                        pairs.append(sym)
            print(pairs)
            #From Coin 1 to Coin 2 - ETH/BTC - Bid
            #From Coin 2 to Coin 3 - ETH/LTC - Ask
            #From Coin 3 to Coin 1 - BTC/LTC - Bid
            arb_list = ['ETH/BTC'] #, 'ETH/LTC', 'BTC/LTC']
            #Find 'closed loop' of currency rate pairs
            j=0
            while 1:
                if j == 1:
                            final = arb_list[0][-3:]  + '/' + str(arb_list[1][-3:])
                            print(final)
                            #if final in symbols:
                            arb_list.append(final)
                            break
                for sym in symbols:
                    if sym in arb_list:
                        pass
                    else:
                        if j % 2 == 0:
                            if arb_list[j][0:3] == sym[0:3]:
                                if arb_list[j] == sym:
                                    pass
                                else:
                                    arb_list.append(sym)
                                    print(arb_list)
                                    j+=1
                                    break
                        if j % 2 == 1:
                            if arb_list[j][-3:] == sym[-3:]:
                                if arb_list[j] == sym:
                                    pass
                                else:
                                    arb_list.append(sym)
                                    print(arb_list)
                                    j+=1
                                    break
            """
                #time.sleep(.5)
        print("List of Arbitrage Symbols:", list_of_sym)
            #time.sleep(3)
        #Determine Rates for our 3 currency pairs - order book
        list_exch_rate_list = []
        if 1:
        #Create Visualization of Currency Exchange Rate Value - Over Time
            #Determine Cycle number (when data is taken) and time when taken
            for k in range(0,cycle_num):
                i=0
                exch_rate_list = []
                print("Data Collection Cycle Number: ", k)
                for sym in list_of_sym:
                    print("Currency Pair: {}".format(sym))
                    if sym in list_of_sym:
                        #depth = client.get_(sym)
                        #print(depth)
                        """if i == 0:      #For first in triangle
                            depth = client.get_order_book(symbol=sym)
                            exch_rate_list.append(float(depth['bids'][0][0]))
                            print(depth['bids'][0][0])
                        """
                        if i % 2==0:
                            #exch_rate_list.append(depth['bids'][0][0]) #converted to Binance
                            depth = client.get_order_book(symbol=sym)
                            inv1 = depth['asks'][0][0]
                            exch_rate_list.append(float(inv1)) #Inverse Because of Binance Format
                            print("Exchange Rate: {}".format(depth['asks'][0][0]))
                        if i == 1:
                            #exch_rate_list.append(depth['asks'][0][0])
                            depth = client.get_order_book(symbol=sym)
                            inv2 = round(1.0/float(depth['bids'][0][0]),6)
                            exch_rate_list.append(float(inv2))      #Inverse because Binance Format
                            print("Exchange Rate: {}".format(depth['bids'][0][0]))
                        i+=1
                    else:
                        exch_rate_list.append(0)

                #exch_rate_list.append(((rateB[-1]-rateA[-1])/rateA[-1])*100)  #Expected Profit
                exch_rate_list.append(datetime.now())      #changed to Human Readable time
                #time.sleep(10)
                #Compare to determine if Arbitrage opp exists
                rate1 = exch_rate_list[0]
                print("Buy: {}".format(rate1))
                rate2 = float(exch_rate_list[2])*float(exch_rate_list[1])
                print("Sell: {}".format(rate2))
                if float(rate1)<float(rate2):
                    print("Arbitrage Possibility")
                    #Calculate Profit, append to List
                    arb_profit = round((float(rate2)-float(rate1))/float(rate2)*100,3)
                    print("Potential Profit (Percentage): {}%".format(arb_profit))
                    exch_rate_list.append(arb_profit)
                else:
                    print("No Arbitrage Possibility")
                    #Add 0 for profit to list
                    exch_rate_list.append(0)
                print(exch_rate_list)
                #Format data (list) into List format (list of lists)
                list_exch_rate_list.append(exch_rate_list)
                time.sleep(cycle_time)
            print(list_exch_rate_list)
            print('ARBITRAGE FUNCTIONALITY SUCCESSFUL - Data of Exchange Rates Collected')
    return exch_rate_list

            #time.sleep(20)

def viz_arb_data(list_exch_rate_list, arb_market, start_time, end_time):
    #Visualize with Matplotlib
    #use matplotlib to plot data
    #Create list from Lists for matplotlib format
    rateA = []      #Original Exchange Rate
    rateB = []      #Calculated/Arbitrage Exchange Rate
    rateB_fee = []  #Include Transaction Fee
    price1 = []     #List for Price of Token (Trade) 1
    price2 = []     #List for price of Token (Trade) 2
    time_list = []  #time of data collection
    profit_list = []     #Record % profit
    for rate in list_exch_rate_list:
        rateA.append(rate[0])
        rateB1 = round(float(rate[1])*float(rate[2]),6)
        rateB.append(rateB1)       #Multiplied together because of Binance Format
        #rateB_fee.append((rate[1]/rate[2])*(1-fee_percentage)*(1-fee_percentage))
        price1.append(rate[1])
        price2.append(rate[2])
        profit_list.append(rate[4])
        time_list.append(rate[3])
    print("Rate A: {} \n Rate B: {} \n Projected Profit (%): {} ".format(rateA, rateB, profit_list)) #rateB_fee))

            #from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
        #Extended 3 axis functionality - https://matplotlib.org/gallery/ticks_and_spines/multiple_yaxis_with_spines.html#sphx-glr-gallery-ticks-and-spines-multiple-yaxis-with-spines-py
            #fig, ax = plt.subplots()
    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()
    par2.spines["right"].set_position(("axes", 1.2))
    make_patch_spines_invisible(par2)
    par2.spines["right"].set_visible(True)
    #Graph Rate & Calculated Rate on Left Hand Side
    p1, = host.plot(time_list, rateA, "k", label = "{}".format(arb_market[0]))
    p1, = host.plot(time_list, rateB, "k+", label = "{} * {}".format(arb_market[1], arb_market[2]))
    #p1, = host.plot(time_list, rateB_fee, 'k+', label = "{} / {} - with Fee".format(arb_list[1], arb_list[2]))
    #Graph Exchange Rate (Originals)
    p2, = par1.plot(time_list, price1, "b-", label="Price - {}".format(arb_market[1]))
    p3, = par2.plot(time_list, price2, "g-", label="Price - {}".format(arb_market[2]))
    #show our graph - with labels
    host.set_xlabel("Time")
    host.set(title='Triangular Arbitrage - Exchange: {}\nStart Time: {}\n End Time: {}\n'
                   'Copyright (c) 2018 @BlockchainEng'.format('Binance', start_time, end_time))
    host.set_ylabel("Exchange Rate")
    par1.set_ylabel("Price - {}".format(arb_market[1]))
    par2.set_ylabel("Price - {}".format(arb_market[2]))
    host.yaxis.label.set_color(p1.get_color())
    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p2, p3]
    host.legend(lines, [l.get_label() for l in lines])  #show Legend
    plt.show()

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


    """

def market_depth(sym, num_entries=20):
    #Get market depth
    #Retrieve and format market depth (order book) including time-stamp
    i=0     #Used as a counter for number of entries
    #print("Order Book: ", convert_time_binance(client.get_server_time()))
    depth = client.get_order_book(symbol=sym)
    print(depth)
    print(depth['asks'][0])
    ask_tot=0.0
    ask_price =[]
    ask_quantity = []
    bid_price = []
    bid_quantity = []
    bid_tot = 0.0
    place_order_ask_price = 0
    place_order_bid_price = 0
    max_order_ask = 0
    max_order_bid = 0
    print("\n", sym, "\nDepth     ASKS:\n")
    print("Price     Amount")
    for ask in depth['asks']:
        if i<num_entries:
            if float(ask[1])>float(max_order_ask):
                #Determine Price to place ask order based on highest volume
                max_order_ask=ask[1]
                place_order_ask_price=round(float(ask[0]),5)-0.0001
            #ask_list.append([ask[0], ask[1]])
            ask_price.append(float(ask[0]))
            ask_tot+=float(ask[1])
            ask_quantity.append(ask_tot)
            #print(ask)
            i+=1
    j=0     #Secondary Counter for Bids
    print("\n", sym, "\nDepth     BIDS:\n")
    print("Price     Amount")
    for bid in depth['bids']:
        if j<num_entries:
            if float(bid[1])>float(max_order_bid):
                #Determine Price to place ask order based on highest volume
                max_order_bid=bid[1]
                place_order_bid_price=round(float(bid[0]),5)+0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            #print(bid)
            j+=1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price
    #Plot Data
"""
if __name__ == "__main__":
    run()
