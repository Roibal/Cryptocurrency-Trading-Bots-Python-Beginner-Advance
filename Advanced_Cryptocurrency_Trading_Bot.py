"""
The Purpose of the RoibalBot Python Program is to create an automated trading bot (functionality) on Binance
Beginner Version Utilized Python-Binance ( https://github.com/sammchardy/python-binance )
Advanced-Version capable of all exchanges, all coins (using ccxt)

Created 4/14/2018 by Joaquin Roibal
V 0.01 - Updated 4/20/2018
v 0.02 - Updated 5/30/2018 - Converted to Advanced Version: https://github.com/Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance

Licensed under MIT License

Introduction Youtube Video: https://www.youtube.com/watch?v=8AAN03M8QhA
Advanced Cryptocurrency Trading Bot: https://www.youtube.com/watch?v=HzibFcWNd-s

Did you enjoy the functionality of this bot? Tips always appreciated.

BTC:
ETH:

NOTE: All Subsequent Version of Program must contain this message, unmodified, in it's entirety
Copyright (c) 2018 by Joaquin Roibal
"""

#import save_historical_data_Roibal
#from binance.client import Client
#from binance.enums import *
import ccxt
import time
import matplotlib.pyplot as plt
import random
from pprint import pprint
#from Keys import Key1

#api_key = BinanceKey1['api_key']
#api_secret = BinanceKey1['api_secret']
#client = Client(api_key, api_secret)

#Get a deposit address for BTC
#address = client.get_deposit_address(asset='BTC')

def run():
    #Initialize Function - Set Initial Conditions for Bot
    arbitrage()
    time.sleep(20)
    initialize()
    #Diversify Funtion - Collect all balances across exchange, then diversify them
    #diversify()
    portfolio = 10  #BTC
    #Active Trader - 'scalping', swing trading, arbitrage
    while 1:
        ActiveTrader()

def arbitrage(cycle_num=5, cycle_time=240):
    #Create Triangular Arbitrage Function
    print("Arbitrage Function Running")
    fee_percentage = 0.001          #divided by 100
    coins = ['BTC', 'LTC', 'ETH']   #Coins to Arbitrage
    #Create Functionality for Binance
    for exch in ccxt.exchanges:    #initialize Exchange
        exchange1 = getattr (ccxt, exch) ()
        symbols = exchange1.symbols
        if symbols is None:
            print("Skipping Exchange ", exch)
            print("\n-----------------\nNext Exchange\n-----------------")
        elif len(symbols)<15:
            print("\n-----------------\nNeed more Pairs (Next Exchange)\n-----------------")
        else:
            print(exchange1)

            exchange1_info = dir(exchange1)
            print("------------Exchange: ", exchange1.id)
            #pprint(exchange1_info)
            print(exchange1.symbols)    #List all currencies
            time.sleep(5)
            #Find Currencies Trading Pairs to Trade
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

                #time.sleep(.5)
            print("List of Arbitrage Symbols:", arb_list)
            #time.sleep(3)
        #Determine Rates for our 3 currency pairs - order book
            list_exch_rate_list = []
        #Create Visualization of Currency Exchange Rate Value - Over Time
            #Determine Cycle number (when data is taken) and time when taken
            for k in range(0,cycle_num):
                i=0
                exch_rate_list = []
                print("Cycle Number: ", k)
                for sym in arb_list:
                    print(sym)
                    if sym in symbols:
                        depth = exchange1.fetch_order_book(symbol=sym)
                        #pprint(depth)
                        if i % 2 == 0:
                            exch_rate_list.append(depth['bids'][0][0])
                        else:
                            exch_rate_list.append(depth['asks'][0][0])
                        i+=1
                    else:
                        exch_rate_list.append(0)
                #exch_rate_list.append(((rateB[-1]-rateA[-1])/rateA[-1])*100)  #Expected Profit
                exch_rate_list.append(time.time())      #change to Human Readable time
                print(exch_rate_list)
                #Compare to determine if Arbitrage opp exists
                if exch_rate_list[0]<exch_rate_list[1]/exch_rate_list[2]:
                    print("Arbitrage Possibility")
                else:
                    print("No Arbitrage Possibility")
                #Format data (list) into List format (list of lists)
                list_exch_rate_list.append(exch_rate_list)
                time.sleep(cycle_time)
            print(list_exch_rate_list)
            #Create list from Lists for matplotlib format
            rateA = []      #Original Exchange Rate
            rateB = []      #Calculated/Arbitrage Exchange Rate
            rateB_fee = []  #Include Transaction Fee
            price1 = []     #List for Price of Token (Trade) 1
            price2 = []     #List for price of Token (Trade) 2
            time_list = []  #time of data collection
            #profit = []     #Record % profit
            for rate in list_exch_rate_list:
                rateA.append(rate[0])
                rateB.append(rate[1]/rate[2])
                rateB_fee.append((rate[1]/rate[2])*(1-fee_percentage)*(1-fee_percentage))
                price1.append(rate[1])
                price2.append(rate[2])
                #profit.append((rateB[-1]-rateA[-1])/rateA[-1])
                time_list.append(rate[3])
            print("Rate A: {} \n Rate B: {} \n Rate C: {} \n".format(rateA, rateB, rateB_fee))
            #Visualize with Matplotlib
            #use matplotlib to plot data
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
            p1, = host.plot(time_list, rateA, "k", label = "{}".format(arb_list[0]))
            p1, = host.plot(time_list, rateB, "k+", label = "{} / {}".format(arb_list[1], arb_list[2]))
            #p1, = host.plot(time_list, rateB_fee, 'k+', label = "{} / {} - with Fee".format(arb_list[1], arb_list[2]))
            #Graph Exchange Rate (Originals)
            p2, = par1.plot(time_list, price1, "b-", label="Price - {}".format(arb_list[1]))
            p3, = par2.plot(time_list, price2, "g-", label="Price - {}".format(arb_list[2]))
            #show our graph - with labels

            host.set_xlabel("Time")
            host.set_ylabel("Exchange Rate")
            par1.set_ylabel("Price - {}".format(arb_list[1]))
            par2.set_ylabel("Price - {}".format(arb_list[2]))
            host.yaxis.label.set_color(p1.get_color())
            tkw = dict(size=4, width=1.5)
            host.tick_params(axis='y', colors=p1.get_color(), **tkw)
            par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
            par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
            host.tick_params(axis='x', **tkw)
            #ax.set(xlabel='Date', ylabel='Exchange Rate', title='Exchange: {}'.format(exch))
            lines = [p1, p2, p3]
            host.legend(lines, [l.get_label() for l in lines])  #show Legend
            plt.show()

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def diversify():
        #Diversify to do (Diversify will diversify portfolio):
            #Collect Amounts in Wallets (available for trading)
    for exch2 in ccxt.exchanges:
        #Change to incorporate requiring API's keys & phrases (from Keys Python Script)
        exch = getattr (ccxt, exch2) ()
        print(exch.fetchBalance())
    #Diversify into pre-described amounts
        # 50% BTC, 5% Each of 8 next-top coins, 10x 1% of micro-caps
    pass

def ActiveTrader():
    #Active Trader - Continuous Loop of calling trader functions such as scalping &
                #arbitrage function
    #Scalping Function
    #Swing Trading Function - Signals
    #Arbitrage Function
    pass

def initialize():
    #Initialize Function - Set Initial Conditions for Bot
    #Get system status
    #Create List of Crypto Pairs to Watch
    all_symbols = []
    micro_cap_coins = []
    #time_horizon = "Short"
    #Risk = "High"
    print("\n\n---------------------------------------------------------\n\n")
    print("Hello and Welcome to the ADVANCED Crypto Trader Bot Python Script\nCreated 2018 by Joaquin Roibal (@BlockchainEng)")
    print("A quick 'run-through' will be performed to introduce you to the functionality of this bot")
    print("To learn more visit medium.com/@BlockchainEng or watch introductory Youtube Videos\n\n")

    time.sleep(5)
    i = 0
    try:
            #Get Status of Exchange & Account
        print("Number of Exchanges: ", len(ccxt.exchanges))
        print("\nList of Available Exchanges: \n \n")
        print(ccxt.exchanges)

            #Get Exchange Info For All Listed Exchanges
        for exch1 in ccxt.exchanges:
            list_of_symbols = []        #Reset List of Symbols for Each Exchange
            if i>0:
                break           #Break Out of Statement
            exch = getattr (ccxt, exch1) ()
                #print(gdax)
            #Secondary Method to Set Exchange
        #exchange1 = ccxt.binance()
            #exchange1_info = dir(exch)
            #pprint(exchange1_info)
            print("\n\nExchange: ", exch.id)
            print("Set Exchange Info (Limits): ", exch.rateLimit)
            print("Load Market: ", exch.load_markets)
            #print(list(exchange1.markets.keys()))
            symbols = exch.symbols
            if symbols is None:
                print("\n-----------------\nNo symbols Loaded\n-----------------")
            else:
                print("-----------------------\nNumber of Symbols: ", len(symbols))
                print("Exchange & Symbols:")
                #print(exchange1.id, exchange1.markets.keys())
                print(exch.id,"-      ", symbols)
                print("-----------------------")
                for sym in symbols:
                    list_of_symbols.append(sym) #Create List of Symbols - Each Exchange
                    all_symbols.append(sym)     #Create List of ALL Symbols on ALL Exchanges
                #print("\n\n'Fetch Orders: ", exchange1.fetch_orders())
                currencies = exch.currencies
                #print("Currencies: ", currencies)
                time.sleep(5)

                #Get Market Depth
                #for symbol in list_of_symbols:
                    #market_depth(symbol)
                #Test Market Order - Visualize - Scalping Functions: Testing with random coin of each exchange
                rand_sym = random.choice(list_of_symbols)
                market_depth(rand_sym, exch)
                visualize_market_depth(sym=rand_sym, exchange=exch)
                scalping_orders(exch, rand_sym)
                i+=1        #Break Out of Initialize Statement
                time.sleep(4)

                """for symbol in exch.markets:
                    print("Order Book for Symbol:     ", symbol)
                    print (exch.fetch_order_book (symbol))
                    time.sleep (3)"""

        #Place a test market buy order, to place an actual order use the create_order function

            #Get Info about Coins in Watch List
        #coin_prices(list_of_symbols)
        #coin_tickers(list_of_symbols)

        #for coin in micro_cap_coins:
        #    visualize_market_depth(1, 1, coin)

        #for coin in micro_cap_coins:
        #    scalping_orders(coin, 1, 1)

            #Get recent trades
        #trades = client.get_recent_trades(symbol='BNBBTC')
        #print("\nRecent Trades: ", trades)
        #print("Local Time: ", time.localtime())
        #print("Recent Trades Time: ", convert_time_binance(trades[0]['time']))

            #Get historical trades
        #hist_trades = client.get_historical_trades(symbol='BNBBTC')
        #print("\nHistorical Trades: ", hist_trades)

            #Get aggregate trades
        #agg_trades = client.get_aggregate_trades(symbol='BNBBTC')
        #print("\nAggregate Trades: ", agg_trades)

        #Example Visualizations of Coins
        """save_historical_data_Roibal.save_historic_klines_csv('BTCUSDT', "1 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_1MINUTE)
        save_historical_data_Roibal.save_historic_klines_csv('ETHBTC', "6 months ago UTC", "now UTC", Client.KLINE_INTERVAL_1DAY)
        save_historical_data_Roibal.save_historic_klines_csv('BRDBNB', "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_3MINUTE)
        save_historical_data_Roibal.save_historic_klines_csv('BTCUSDT', "12 months ago UTC", "now UTC", Client.KLINE_INTERVAL_1WEEK)
        save_historical_data_Roibal.save_historic_klines_csv('ETHUSDT', "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_15MINUTE)

        #Visualize All Micro Cap Coins for 8 hour period and 3 minute Candlestick
        for coin in micro_cap_coins:
            save_historical_data_Roibal.save_historic_klines_csv(coin, "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_3MINUTE)
            save_historical_data_Roibal.save_historic_klines_csv(coin, "24 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_15MINUTE)
            save_historical_data_Roibal.save_historic_klines_csv(coin, "1 month ago UTC", "now UTC", Client.KLINE_INTERVAL_1DAY)
        """
        print("INITIALIZE SUCCESSFUL")
    except():
        print("\n \n \nATTENTION: NON-VALID CONNECTION WITH CRYPTOCURRENCY BOT \n \n \n")

            #Account Withdrawal History Info
        #withdraws = client.get_withdraw_history()
        #print("\nClient Withdraw History: ", withdraws)


def market_depth(sym, exchange=ccxt.binance(), num_entries=20):
    #Get market depth
    #Retrieve and format market depth (order book) including time-stamp
    i=0     #Used as a counter for number of entries
    print("Order Book: ") #convert_time_binance(client.get_server_time()))   #Transfer to CCXT
    exchange.verbose = True
    depth = exchange.fetch_order_book(symbol=sym)               #Transf'd to CCXT
    #pprint(depth)
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
    print("\n", sym, "\nDepth     ASKS:\n")         #Edit to work with CCXT
    print("Price     Amount")
    for ask in depth['asks']:
        if i<num_entries:
            if float(ask[1])>float(max_order_ask):
                #Determine Price to place ask order based on highest volume
                max_order_ask=ask[1]
                #print("Max Order ASK: ", max_order_ask)
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
                #print("Max Order BID: ", max_order_bid)
                place_order_bid_price=round(float(bid[0]),5)+0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            #print(bid)
            j+=1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price
    #Plot Data

def scalping_orders(exchange = ccxt.binance(), coin='BTC/USDT', wait=1, tot_time=1):
    #Function for placing 'scalp orders'
    #Calls on Visualizing Scalping Orders Function
    ap, aq, bp, bq, place_ask_order, place_bid_order, spread, proj_spread, max_bid, min_ask = visualize_market_depth(wait, tot_time, coin, 5, exchange)
    print("Coin: {}\nPrice to Place Ask Order: {}\nPrice to place Bid Order: {}".format(coin, place_ask_order, place_bid_order))
    print("Spread: {} % Projected Spread {} %".format(spread, proj_spread))
    print("Max Bid: {} Min Ask: {}".format(max_bid, min_ask))
    #Place Orders based on calculated bid-ask orders if projected > 0.05% (transaction fee)
    #Documentation: http://python-binance.readthedocs.io/en/latest/account.html#orders
    """
    if proj_spread > 0.05:
        quant1=100          #Determine Code Required to calculate 'minimum' quantity
        #Place Bid Order:
        bid_order1 = client.order_limit_buy(
            symbol=coin,
            quantity=quant1,
            price=place_bid_order)
        #Place Ask Order
        ask_order1 = client.order_limit_sell(
            symbol=coin,
            quantity=quant1,
            price=place_ask_order)


    #Place second order if current spread > 0.05% (transaction fee)

    """


def visualize_market_depth(wait_time_sec='1', tot_time='1', sym='BTC/USDT', precision=5, exchange=ccxt.binance()):
    cycles = int(tot_time)/int(wait_time_sec)
    start_time = time.asctime()         #Trans CCXT
    fig, ax = plt.subplots()
    for i in range(1,int(cycles)+1):
        ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order = market_depth(sym, exchange)

        #print(ask_price)
        plt.plot(ask_pri, ask_quan, color = 'red', label='asks-cycle: {}'.format(i))
        plt.plot(bid_pri, bid_quan, color = 'blue', label = 'bids-cycle: {}'.format(i))

        #ax.plot(depth['bids'][0], depth['bids'][1])
        max_bid = max(bid_pri)
        min_ask = min(ask_pri)
        max_quant = max(ask_quan[-1], bid_quan[-1])
        spread = round(((min_ask-max_bid)/min_ask)*100,5)   #Spread based on market
        proj_order_spread = round(((ask_order-bid_order)/ask_order)*100, precision)
        price=round(((max_bid+min_ask)/2), precision)
        plt.plot([price, price],[0, max_quant], color = 'green', label = 'Price - Cycle: {}'.format(i)) #Vertical Line for Price
        plt.plot([ask_order, ask_order],[0, max_quant], color = 'black', label = 'Ask - Cycle: {}'.format(i))
        plt.plot([bid_order, bid_order],[0, max_quant], color = 'black', label = 'Buy - Cycle: {}'.format(i))
        #plt.plot([min_ask, min_ask],[0, max_quant], color = 'grey', label = 'Min Ask - Cycle: {}'.format(i))
        #plt.plot([max_bid, max_bid],[0, max_quant], color = 'grey', label = 'Max Buy - Cycle: {}'.format(i))
        ax.annotate("Max Bid: {} \nMin Ask: {}\nSpread: {} %\nCycle: {}\nPrice: {}"
                    "\nPlace Bid: {} \nPlace Ask: {}\n Projected Spread: {} %".format(max_bid, min_ask, spread, i, price, bid_order, ask_order, proj_order_spread),
                    xy=(max_bid, ask_quan[-1]), xytext=(max_bid, ask_quan[0]))
        if i==(cycles+1):
            break
        else:
            time.sleep(int(wait_time_sec))
    #end_time = time.asctime()
    ax.set(xlabel='Price', ylabel='Quantity',
       title='{} Order Book: {} \n {}\n Cycle Time: {} seconds - Num Cycles: {}'.format(exchange.id, sym, start_time, wait_time_sec, cycles))
    plt.legend()
    plt.show()
    return ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order, spread, proj_order_spread, max_bid, min_ask


def coin_prices(watch_list):
    #Will print to screen, prices of coins on 'watch list'
    #returns all prices
    prices = client.get_all_tickers()           #Trans CCXT
    print("\nSelected (watch list) Ticker Prices: ")
    for price in prices:
        if price['symbol'] in watch_list:
            print(price)
    return prices


def coin_tickers(watch_list):
    # Prints to screen tickers for 'watch list' coins
    # Returns list of all price tickers
    tickers = client.get_orderbook_tickers()            #Trans CCXT
    print("\nWatch List Order Tickers: \n")
    for tick in tickers:
        if tick['symbol'] in watch_list:
            print(tick)
    return tickers

def portfolio_management(deposit = '10000', withdraw=0, portfolio_amt = '0', portfolio_type='USDT', test_acct='True'):
    """The Portfolio Management Function will be used to track profit/loss of Portfolio in Any Particular Currency (Default: USDT)"""
    #Maintain Portfolio Statistics (Total Profit/Loss) in a file
    pass

def Bollinger_Bands():
    #This Function will calculate Bollinger Bands for Given Time Period
    pass

def buy_sell_bot():
    pass

def position_sizing():
    pass

def trailing_stop_loss():
    pass

if __name__ == "__main__":
    run()
