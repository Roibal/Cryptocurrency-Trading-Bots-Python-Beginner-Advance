"""
The Purpose of the PrivateBinance Arbitrage Bot (based on RoibalBot) Python Program is to create an automated trading bot (functionality) on Binance
Utilized Python-Binance ( https://github.com/sammchardy/python-binance ) (NOTE: Use Roibal Fork of Python Binance)
Advanced-Version capable of all exchanges, all coins (using cctx)

This 'bot' will run a functionality which seeks profitable triangular arbitrage opportunities on Binance
Weekly/Daily/Hourly reports created on profit/loss

Instructional Youtube Video: https://www.youtube.com/watch?v=8AAN03M8QhA - Additional Videos Available on youtube

Created 4/14/2018 by Joaquin Roibal
V 0.01 - Updated 4/20/2018
v 0.02 - Updated 5/30/2018 - Converted to Advanced Version: https://github.com/Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance
v 0.03 - Created 6/18/2018 - Binance Arbitrage Bot
v 0.04 - 6/21/2018 - Changed Name to CryptoTriangularArbitrageBinanceBot.py
v 1.00 - 6/24/2018 - Converted to Private_TriArbBot.py for Private Trader Group
v 1.01 - 6/27/2018 - Incorporated Fees & Live Trading Functionality
v 1.02 - 6/27/2018 - Fixed Order Functionality, Order Amounts, Fee Calculation
v 1.03 - 6/27/2018 - Converted to Paper & Tweet format - will collect, save data & tweet every few minutes

All Rights Reserved

ATTENTION: BY RUNNING SCRIPT YOU AGREE TO REMIT 1% of PROFITS TO THE FOLLOWING ADDRESS DAILY:
BTC: 1BYrAED4pi5DMKu2qZPv8pwe6rEeuxoCiD

NOTE: All Subsequent Version of Program must contain this message, unmodified, in it's entirety
Copyright (c) 2018 by Joaquin Roibal
"""

from binance.client import Client
from binance.enums import *
import time
from datetime import datetime
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
#import pprint
#import win32api
#import save_historical_data_Roibal
import math
from BinanceKeys import BinanceKey1
import pprint
import tweepy

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']
#load twitter instantiating code
#Oauth consumer key/secret and token/secret from twitter application
consumer_key =
consumer_secret =
access_token =
access_token_secret =

#Authorization for Tweepy format
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


client = Client(api_key, api_secret)
print(client)
#client.synced('order_market_buy', symbol='BNBBTC', quantity=10)

def run():
    #set_time_binance()
    #Initialize Arbitrage Binance Bot on Infinite Loop
    while 1:
        initialize_arb()


    #Perform our Arbitrage Function

    #Data Output (log) in a text file - keep track of start/end time, trades, balance
    pass

def set_time_binance():
    #Code By Khal Q
    gt=client.get_server_time()
    tt=time.gmtime(int((gt["serverTime"])/1000))
    #win32api.SetSystemTime(tt[0], tt[1],0,tt[2], tt[3], tt[4],tt[5],0)
def initialize_arb():

    welcome_message = "\n\n---------------------------------------------------------\n\n"
    welcome_message+= "Hello and Welcome to the Binance Arbitrage Crypto Trader Bot Python Script\nCreated 2018 by Joaquin Roibal (@BlockchainEng)"
    welcome_message+= "A quick 'run-through' will be performed to introduce you to the functionality of this bot\n"
    welcome_message+="To learn more visit medium.com/@BlockchainEng or watch introductory Youtube Videos"
    welcome_message+="\nCopyright 2018 by Joaquin Roibal\n"
    bot_start_time = str(datetime.now())
    welcome_message+= "\nBot Start Time: {}\n\n\n".format(bot_start_time)
    print(welcome_message)
    #info = client.get_account()
    #Clear All Pending Trades

    #print(info)
    #welcome_message+=str(info)
    time.sleep(5)
    #trades = client.get_my_trades(symbol='BNBBTC')
    #print(trades)
    #data_log_to_file(balance)

    #output to file - create function
    data_log_to_file(welcome_message)
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
        coin_list = ['BTC', 'ETH', 'USDT', 'BNB', 'THETA', 'NANO']
        balance_list = []
        #for coin in coin_list:
        #    balance_list.append(client.get_asset_balance(coin))
        print(balance_list)
        data_log_to_file(str(balance_list))
        list_of_symbols = ['BNBBTC', 'THETABNB', 'THETABTC']
        list_of_symbols2 = ['BNBBTC', 'NANOBNB', 'NANOBTC']
        list_of_symbols22 = ['BNBBTC', 'CVCBNB', 'CVCBTC']
        list_of_symbols3 = ['BTCUSDT', 'BNBBTC', 'BNBUSDT']
        list_of_symbols4 = ['ETHBTC', 'BNBETH', 'BNBBTC']
        list_of_symbols5 = ['ETHUSDT', 'BNBETH', 'BNBUSDT']
        list_of_arb_sym = [list_of_symbols, list_of_symbols2, list_of_symbols22, list_of_symbols3, list_of_symbols4, list_of_symbols5]

        #Create List of all balance amounts for each coin:
        msg1 = "LOADING BALANCES FROM BINANCE"
        #Get Binance Wallet Balance - Split into 4 coins evenly
        print(msg1)
        data_log_to_file(msg1)
        list_balance = []
        #for sym in list_of_arb_sym:
            #for sym2 in sym:
            #    orders = client.get_all_orders(symbol=sym2, limit=10)
            #    list_balance.append(orders)
        #data_log_to_file(list_balance)
        #pprint(list_balance)

            #info = client.get_symbol_info(sym)
            #print(info)
        #prices = client.get_all_tickers()
        tickers = client.get_orderbook_tickers()
        #print(prices)
        #print(tickers)
        #portfolio = [10, 100, 10000, 500, str(datetime.now())] #Number of: [Bitcoin, Ethereum, USDT, Binance Coin]
        #Load Binance Portfolio
        #binance_portfolio(coin_list)
        #Load Portfolio File
        portfolio=[]
        msg="Crypto Trading Bot - Arbitrage Market Analysis"
        with open('Portfolio.txt') as f1:
            read_data = f1.readlines()
            for line in read_data:
                load_portfolio = line       #Load Previous Portfolio
        load_portfolio = list(load_portfolio[1:-1].split(','))
        #Load From Binance
        #print(load_portfolio)
        #time.sleep(5)
        #for i in range(0,3):
            #portfolio[i] = float(portfolio[i])      #Set Type for first 4 values of Portfolio
        i=0
        for val in load_portfolio:
            #print(val.strip())
            if i == 4:
                portfolio.append(str(datetime.now()))
                break
            portfolio.append(float(val.strip()))
            i+=1
        portf_msg = "Starting Portfolio (Paper): " + str(portfolio)
        #Load Balances for each coin in exchange
        #Split BTC into 4 equal amounts, buy all 3 other coins with that amount
        print(portf_msg)
        portf_file_save(portfolio)
        data_log_to_file(portf_msg)
        while 1:
            #Run Arbitrage Profit Functionality - To Determine Highest Profit Percentage - Cont Loop
            calc_profit_list =[]
            for arb_market in list_of_arb_sym:
                arb_bin, j = arbitrage_bin(arb_market, tickers, portfolio, 1, 1)
                calc_profit_list.append(arb_bin)

            for profit1 in calc_profit_list:
                data_log_to_file(str(profit1))
            print(calc_profit_list)
            exp_profit = 0      #Expected Profit, Set to 0 initially
            m = n = 0       #Market Position Market
            for exch_market in calc_profit_list:
                if exch_market[4]>exp_profit:
                    exp_profit = exch_market[4]
                    m = n
                n+=1
            profit_message = "\nMost Profitable Market: {} \nExpected Profit: {}%".format(list_of_arb_sym[m], exp_profit)
            print(profit_message)
            msg+= profit_message
            data_log_to_file(profit_message)
            time.sleep(15)
            #Run Arbitrage Function on Highest Profit Percentage Coin for 10 minutes
            arb_list_data = []
            arb_start_time = str(datetime.now())
            for i in range(0,45):
                #Collect Arbitrage Data Into List format for 5 cycles, 30 second cycles (replaces functionality)

                try:
                    arb_bin2, j2 = arbitrage_bin(list_of_arb_sym[m], tickers, portfolio, 1, 1, 'No', 'No')
                    arb_list_data.append(arb_bin2)   #'Yes' to place orders
                    #binance_portfolio(coin_list)
                except:
                    raise
                    pass
                #print(arb_l    ist_data)
                time.sleep(30)
            arb_end_time = str(datetime.now())
            #Visualize Collected Arb List Data with MatPlotLib
            #msg+=profit_message
            data_log_to_file(msg)   #Save to Output the Message to be tweeted
            viz_arb_data(arb_list_data, list_of_arb_sym[m], arb_start_time, arb_end_time, 'Yes', msg)   #Add 'Yes' for tweet
    except:
        print("\nFAILURE INITIALIZE\n")
        raise

def data_log_to_file(message):
    with open('CryptoTriArbBot_DataLog.txt', 'a+') as f:
        f.write(message)

def portf_file_save(portfolio, filename='Portfolio.txt'):
    with open(filename, 'a+') as f:
        f.write('\n'+str(portfolio))

def arbitrage_bin(list_of_sym, tickers, portfolio, cycle_num=10, cycle_time=30, place_order='No', real_order='No', msg = []):
    #Create Triangular Arbitrage Function
    arb_message = "Beginning Binance Arbitrage Function Data Collection - Running\n"
    print(arb_message)
    data_log_to_file(arb_message)
    #time.sleep(2)
    fee_percentage = 0.05*3          #divided by 100
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
                profit_fee_list = []
                data_collect_message1 = "Data Collection Cycle Number: "+str(k) +'\n'
                #print(data_collect_message1)
                data_log_to_file(data_collect_message1)
                for sym in list_of_sym:
                    currency_pair = "Currency Pair: "+str(sym)+" "
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
                            Exch_rate1 = currency_pair+ "Exchange Rate: {}".format(depth['asks'][0][0]) +' '
                            print(Exch_rate1)
                            data_log_to_file(Exch_rate1)
                        if i == 1:
                            #exch_rate_list.append(depth['asks'][0][0])
                            depth = client.get_order_book(symbol=sym)
                            inv2 = round(1.0/float(depth['bids'][0][0]),6)
                            exch_rate_list.append(float(inv2))      #Inverse because Binance Format
                            Exch_rate2 = currency_pair+"Exchange Rate: {}".format(depth['bids'][0][0])+' '
                            print(Exch_rate2)
                            data_log_to_file(Exch_rate2)
                        i+=1
                    else:
                        exch_rate_list.append(0)

                #exch_rate_list.append(((rateB[-1]-rateA[-1])/rateA[-1])*100)  #Expected Profit
                exch_rate_list.append(datetime.now())      #changed to Human Readable time
                #time.sleep(10)
                #Compare to determine if Arbitrage opp exists
                rate1 = exch_rate_list[0]
                buy_price = "Buy: {}".format(rate1)
                print(buy_price)
                data_log_to_file(buy_price)
                rate2 = float(exch_rate_list[2])*float(exch_rate_list[1])
                sell_price = "Sell: {}".format(rate2)
                print(sell_price)
                data_log_to_file(sell_price)
                if float(rate1)<float(rate2):
                    arb_1_msg = "Arbitrage Possibility - "
                    #Calculate Profit, append to List
                    arb_profit = round((float(rate2)-float(rate1))/float(rate2)*100,3)

                    arb_profit_fees = fee_percentage
                    arb_profit_adjust = arb_profit - arb_profit_fees
                    arb_1_msg += "Potential Profit (Percentage): "+str(arb_profit) +'%\n'
                    arb_1_msg += "\nPotential Fees (Percentage): "+str((arb_profit_fees))
                    arb_1_msg += "\nAdjusted Profit (Percentage): "+str(arb_profit_adjust)
                    print(arb_1_msg)
                    #msg+=arb_1_msg
                    data_log_to_file(arb_1_msg)
                    exch_rate_list.append(arb_profit)
                    profit_fee_list.append([arb_profit, arb_profit_fees, arb_profit_adjust])
                    portf_file_save(profit_fee_list, 'Portfolio_fees_Rates.txt')
                    #Calculate Amount Profit (orderbooks)
                    #Place Order (Play Money)
                    if place_order == 'Yes':
                        place_order_msg = "PLACING ORDER"
                        print(place_order_msg)
                        data_log_to_file(place_order_msg)
                        portfolio, start, coin2, coin3, final = tri_arb_paper(portfolio, list_of_sym, exch_rate_list)
                        portfolio2, start1, coin2fee, coin3fee, final  = tri_arb_paper(portfolio, list_of_sym, exch_rate_list, 'Yes')
                        #portfolio_strat1 = tri_arb_paper(portfolio, list_of_sym, exch_rate_list, 'Yes')
                        if arb_profit_adjust>0:
                            portf_file_save(portfolio2, "Portfolio_fees_strategy1.txt")
                        portf_file_save(portfolio)
                        portf_file_save(portfolio2, 'Portfolio_fees.txt')
                        #If Function is submitted requesting 'Real Order'
                        if real_order == 'Yes':
                            if arb_profit>fee_percentage:
                                real_order_msg = "ENTERING REAL ORDER: "
                                real_order_msg += "NO FEE PROFIT PERCENTAGE: "+str(arb_profit)
                                real_order_msg += "FEE PERCENTAGE: "+str(fee_percentage)
                                real_order_msg += "ARBITRAGING: "+str(list_of_sym)
                                print(real_order_msg)
                                msg+= real_order_msg
                                data_log_to_file(real_order_msg)
                                #Place 3 orders in succession buying/selling coins for the tri arb
                                quantity = [0.005, 0.21, 15, 1, 60, 60, 60]       #Limit Amounts For Trading
                                real_order_msg1 = "REAL ORDER BUY (1): " +str(list_of_sym[0])
                                port, amt_coin1, amt_coin2, amt_coin3, amt_coin_final = tri_arb_paper(quantity, list_of_sym, exch_rate_list, 'Yes')
                                coin_amts = [amt_coin1, amt_coin2[-1], amt_coin3[-1], amt_coin_final[-1]]
                                #Round Coin Amounts of Binance Coin (must be purchased in whole amounts)
                                for a, sym in enumerate(list_of_sym):
                                    print(sym)
                                    if sym[0:3]=='BNB' or sym[-3:]=='BNB':
                                        coin_amts[a+1] = math.ceil(coin_amts[a+1])
                                        print(coin_amts[a])
                                real_order_msg1 += "Coin Amounts to Purchase: "+str(coin_amts)
                                print(real_order_msg1)
                                real_order_start_time = datetime.now()
                                real_order_msg1+="\nSTART TIME: " + str(real_order_start_time)+"\n\n"
                                #First Order - Coin 2 from Starting Coin -
                                price_order_1 = round(float(exch_rate_list[int(0)]),5)
                                quantity_1 = round(coin_amts[1], 5)
                                order_1 = client.create_order (symbol=list_of_sym[0],
                                                    side=SIDE_BUY,
                                                    type=ORDER_TYPE_LIMIT,
                                                    quantity=quantity_1,
                                                    price=price_order_1,
                                                    timeInForce=TIME_IN_FORCE_GTC)
                                real_order_msg1 += str(order_1) +'\n'+str(quantity_1)

                                price_order_2 = round((1/exch_rate_list[1]), 5)
                                print(price_order_2)
                                quantity_2 = round(coin_amts[2], 5)
                                order_2 = client.create_order (symbol=list_of_sym[1],
                                                    side=SIDE_BUY,
                                                    type=ORDER_TYPE_LIMIT,
                                                    quantity=quantity_2,
                                                    price=price_order_2,
                                                    timeInForce=TIME_IN_FORCE_GTC)
                                real_order_msg1 += str(order_2)+'\n'+str(quantity_2)
                                real_order_msg1 += "\n\nREAL ORDER SELL: \n"
                                price_order_3 = round(float(exch_rate_list[int(2)]),5)
                                quantity_3 = round(coin_amts[3], 5)
                                order_3 = client.create_order (symbol=list_of_sym[2],
                                                    side=SIDE_SELL,
                                                    type=ORDER_TYPE_LIMIT,
                                                    quantity=quantity_3,
                                                    price=price_order_3,
                                                    timeInForce=TIME_IN_FORCE_GTC)
                                real_order_msg1+= str(order_3)+'\n'+str(quantity_3)
                                real_order_stop_time = datetime.now()
                                real_order_msg1+= str(real_order_stop_time)
                                portf_file_save(real_order_msg, 'Real_Order_Messages_Log.txt')
                                real_order_msg_prices = [price_order_1, price_order_2, price_order_3]
                                real_order_quantity = [quantity_1, quantity_2, quantity_3]
                                real_order_msg_prices+=real_order_quantity
                                real_order_msg_prices.append(datetime.now())
                                real_order_msg1+= real_order_msg_prices
                                print(real_order_msg1)
                                list_of_orders = [order_1, order_2, order_3]
                                    #plc_order_msg = "Placing Order: "+ str(order)
                                for plc_order_msg in list_of_orders:
                                    portf_file_save(plc_order_msg, 'PlaceOrderLog.txt')
                                for prices in real_order_msg_prices:
                                    portf_file_save(real_order_msg_prices, 'RealOrderPrices.txt')
                                data_log_to_file(real_order_msg1)
                        #Call function that will paper-trade with portfolio
                        #portfolio = list(portfolio)
                        portfolio = tri_arb_paper(portfolio, list_of_sym, exch_rate_list)
                        portf_file_save(portfolio)
                else:
                    arb_2_msg = "No Arbitrage Possibility"
                    print(arb_2_msg)
                    data_log_to_file(arb_2_msg)
                    #Add 0 for profit to list
                    exch_rate_list.append(0)
                exch_msg = "Exchange Rate List: " +str(exch_rate_list)+'\n'
                #for exch_list in exch_rate_list:
                #print(exch_msg)
                data_log_to_file(exch_msg)
                #Format data (list) into List format (list of lists)
                #list_exch_rate_list.append(exch_rate_list)
                time.sleep(cycle_time)
            #print(list_exch_rate_list)
            print('\nARBITRAGE FUNCTIONALITY SUCCESSFUL - Data of Exchange Rates Collected\n')
    return exch_rate_list, msg

def tri_arb_paper(portfolio1, sym_list, list_exch_rates, fees='No', fee=0.0005):
    #Determine Which Coin Starting With
    tri_arb_paper_msg = "\nSTARTING TRI ARB PAPER TRADING FUNCTION\n"
    print(tri_arb_paper_msg)
    #print(portfolio1)
    #time.sleep(10)
    data_log_to_file(tri_arb_paper_msg)
    if sym_list[0][-3:]=='BTC':
        portf_pos = 0
    elif sym_list[0][-3:]=='ETH':
        portf_pos = 1
    elif sym_list[0][-3:]=='SDT':
        portf_pos = 2
    elif sym_list[0][-3:]=='BNB':
        portf_pos = 3
    elif sym_list[0][-3:]=='ANO':
        portf_pos = 4
    elif sym_list[0][-3:]=='ETA':
        portf_pos = 5
    elif sym_list[0][-3:]=='CVC':
        portf_pos = 6
    if fees == 'Yes':
        start_amount = float(portfolio1[portf_pos])
        amt_coin2 = start_amount / float(list_exch_rates[0])
        amt_coin2_no_fee = amt_coin2
        amt_coin2_fee = amt_coin2*fee
        amt_coin2_adj = amt_coin2*(1-fee)
        amt_coin3 = amt_coin2_adj * float(list_exch_rates[1])
        amt_coin3_no_fee = amt_coin2_no_fee*float(list_exch_rates[1])
        amt_coin3_fee = amt_coin3 * fee
        amt_coin3_adj = amt_coin3*(1-fee)
        final_amount = amt_coin3_adj * float(list_exch_rates[2])
        final_amount_no_fee = amt_coin3_no_fee * float(list_exch_rates[2])
        final_amount_fee = final_amount *fee
        final_amount_adj = final_amount *(1-fee)
        tri_arb_paper_msg = "Starting Amount: "+str(sym_list[0][-3:])+" "+str(start_amount)+'\n'
        #Buy Currency 2 with Currency 1
        tri_arb_paper_msg += "\nAmount Coin 2: "+str(sym_list[0][0:3])+" "+str(amt_coin2)+'\n'
        tri_arb_paper_msg += "\nAmount Coin 2 (no fee): "+str(sym_list[0][0:3])+" "+str(amt_coin2_no_fee)+'\n'
        tri_arb_paper_msg += "\nAmount Coin 2 Fee: "+str(sym_list[0][0:3])+" "+str(amt_coin2_fee)+'\n'
        tri_arb_paper_msg += "\nAmount Coin 2 Adjusted: "+str(sym_list[0][0:3])+" "+str(amt_coin2_adj)+'\n'
        #Buy Currency 3 with Currency 2
        tri_arb_paper_msg += "\nAmount Coin 3: "+str(sym_list[2][0:3])+" "+str(amt_coin3) +'\n'
        tri_arb_paper_msg += "\nAmount Coin 3 (no fee): "+str(sym_list[2][0:3])+" "+str(amt_coin3_no_fee) +'\n'
        tri_arb_paper_msg += "\nAmount Coin 3 Fee: "+str(sym_list[2][0:3])+" "+str(amt_coin3_fee)+'\n'
        tri_arb_paper_msg += "\nAmount Coin 3 Adjusted: "+str(sym_list[2][0:3])+" "+str(amt_coin3_adj)+'\n'
        #Buy Currency 1 with Currency 3
        tri_arb_paper_msg += "\nFinal Amount: "+str(sym_list[0][-3:])+" "+str(final_amount)+'\n'
        tri_arb_paper_msg += "\nFinal Amount (No Fee): "+str(sym_list[0][-3:])+" "+str(final_amount_no_fee)+'\n'
        tri_arb_paper_msg += "\nFinal Amount Fee: "+str(sym_list[0][-3:])+" "+str(final_amount_fee)+'\n'
        tri_arb_paper_msg += "\nFinal Amount Adjusted: "+str(sym_list[0][-3:])+" "+str(final_amount_adj)+'\n'
        #Create Log of 'Volume' and Transfer
        #Volume(Total Paid), Fee, Final Amount
        coin2_fee_amounts = [amt_coin2, amt_coin2_no_fee, amt_coin2_fee, amt_coin2_adj]
        coin3_fee_amounts = [amt_coin3, amt_coin3_no_fee, amt_coin3_fee, amt_coin3_adj]
        final_coin_fee_amounts = [final_amount, final_amount_no_fee, final_amount_fee, final_amount_adj]
        list_of_fees = [coin2_fee_amounts, coin3_fee_amounts, final_coin_fee_amounts]
        print(tri_arb_paper_msg)
        print(list_of_fees)
        data_log_to_file(str(list_of_fees))
        for fee in list_of_fees:
            portf_file_save(fee, 'list_fees_paid.txt')
        data_log_to_file(tri_arb_paper_msg)
        portfolio1[portf_pos] = final_amount_adj
        portfolio1[-1] = str(datetime.now())
    if fees == 'No':
        start_amount = float(portfolio1[portf_pos])
        coin2_fee_amounts = coin3_fee_amounts = final_coin_fee_amounts =  [0, 0, 0, 0]  #Blank List for these values if Fees = 'No'
        amt_coin2 = start_amount / float(list_exch_rates[0])
        amt_coin3 = amt_coin2 * float(list_exch_rates[1])
        final_amount = amt_coin3 * float(list_exch_rates[2])
        tri_arb_paper_msg = "Starting Amount: "+str(sym_list[0][-3:])+" "+str(start_amount)+'\n'
        #Buy Currency 2 with Currency 1
        tri_arb_paper_msg += "Amount Coin 2: "+str(sym_list[0][0:3])+" "+str(amt_coin2)+'\n'
        #Buy Currency 3 with Currency 2
        tri_arb_paper_msg += "Amount Coin 3: "+str(sym_list[2][0:3])+" "+str(amt_coin3) +'\n'
        #Buy Currency 1 with Currency 3
        tri_arb_paper_msg += "Final Amount: "+str(sym_list[0][-3:])+" "+str(final_amount)+'\n'
        print(tri_arb_paper_msg)
        data_log_to_file(tri_arb_paper_msg)
        portfolio1[portf_pos] = final_amount
        portfolio1[-1] = str(datetime.now())

    return portfolio1 , start_amount, coin2_fee_amounts, coin3_fee_amounts, final_coin_fee_amounts

    """
    start_amount = float(portfolio1[portf_pos])
    amt_coin2 = start_amount / float(list_exch_rates[0])
    amt_coin3 = amt_coin2 * float(list_exch_rates[1])
    final_amount = amt_coin3 * float(list_exch_rates[2])
    tri_arb_paper_msg = "Starting Amount: "+str(sym_list[0][-3:])+" "+str(start_amount)+' '
    #Buy Currency 2 with Currency 1
    tri_arb_paper_msg += "Amount Coin 2: "+str(sym_list[0][0:3])+" "+str(amt_coin2)+' '
    #Buy Currency 3 with Currency 2
    tri_arb_paper_msg += "Amount Coin 3: "+str(sym_list[2][0:3])+" "+str(amt_coin3) +' '
    #Buy Currency 1 with Currency 3
    tri_arb_paper_msg += "Final Amount: "+str(sym_list[0][-3:])+" "+str(final_amount)+' '
    print(tri_arb_paper_msg)
    data_log_to_file(tri_arb_paper_msg)
    portfolio1[portf_pos] = final_amount
    portfolio1[-1] = str(datetime.now())
    return portfolio1
    """

def viz_arb_data(list_exch_rate_list, arb_market, start_time, end_time, Tweet_message='No', msg = []):
    viz_msg = "\nARBITRAGE VIZ FUNCTIONALITY\n"
    print(viz_msg)
    #msg+=viz_msg
    data_log_to_file(viz_msg)
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
    viz_msg2 = "Rate A: {} \n Rate B: {} \n Projected Profit (%): {} ".format(rateA, rateB, profit_list) #rateB_fee))
    print(viz_msg2)
    data_log_to_file(viz_msg2)

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
    host.set(title='Triangular Arbitrage - Exchange: {}\nStart Time: {} End Time: {}\n'
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
    fname = "Binance_Test.png"  #+"-"+str(arb_market[0])+str(arb_market[1])+str(arb_market[2])+".png"
    #Future: Include Start/End Time
    plt.savefig(fname) #Changes to make - Format
    """, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)"""
    print_figure_message = "Data Collected Figure Printed & Saved - " + str(fname)
    print(print_figure_message)
    data_log_to_file(print_figure_message)
    #plt.show()
    #Add Functionality that will tweet message with graph as well.
    if Tweet_message == 'Yes':
        #msg+=viz_msg2
        msg+= "\nStart Time: "+str(start_time)+ " End Time: " +str(end_time)
        msg+="\n\nvia @BlockchainEng & @CryptoTrade_Bot \n\n #Crypto #BTC"
        print(msg) #Tweet this message then upload file
        #Tweet msg and Upload the Graph of last time period directly to twitter
        print("TWITTER PREVIEW: ", msg)
        try:
            api.update_with_media(fname, status=msg)
        except:
            data_log_to_file('ERROR:  TWITTER ERROR')
            pass
        data_log_to_file("TWEET MESSAGE: " +str(msg))
        #Upload File (Latest Visualization: 'fname')


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
