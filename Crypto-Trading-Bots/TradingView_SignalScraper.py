"""
A python script/bot which will collect (scrape) TradingView Signals for a list of coins.
Original Code by Michael Goode
Modified 7/15/2018 by Joaquin Roibal (@BlockchainEng)

"""

import requests, json, time, datetime
from BinanceKeys import BinanceKey1
import tweepy
from samplekeys import keys, keys2, keys3, rkey

api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']
#load twitter instantiating code
list_of_accts = [keys, keys2, keys3]
#Oauth consumer key/secret and token/secret from twitter application
consumer_key = keys3['consumer_key']
consumer_secret = keys3['consumer_secret']

access_token = keys3['access_token']
access_token_secret = keys3['access_token_secret']

#Authorization for Tweepy format
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def mlog(market, *text):
	text = [str(i) for i in text]
	text = " ".join(text)

	datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

	print("[{} {}] - {}".format(datestamp, market, text))


def get_signal(market, candle):
	headers = {'User-Agent': 'Mozilla/5.0'}
	url = "https://scanner.tradingview.com/crypto/scan"

	payload =	{
					"symbols": {
						"tickers": ["BINANCE:{}".format(market)],
						"query": { "types": [] }
					},
					"columns": [
						"Recommend.Other|{}".format(candle),
						"Recommend.All|{}".format(candle),
						"Recommend.MA|{}".format(candle),
						"RSI|{}".format(candle),
						"RSI[1]|{}".format(candle),
						"Stoch.K|{}".format(candle),
						"Stoch.D|{}".format(candle),
						"Stoch.K[1]|{}".format(candle),
						"Stoch.D[1]|{}".format(candle),
						"CCI20|{}".format(candle),
						"CCI20[1]|{}".format(candle),
						"ADX|{}".format(candle),
						"ADX+DI|{}".format(candle),
						"ADX-DI|{}".format(candle),
						"ADX+DI[1]|{}".format(candle),
						"ADX-DI[1]|{}".format(candle),
						"AO|{}".format(candle),
						"AO[1]|{}".format(candle),
						"Mom|{}".format(candle),
						"Mom[1]|{}".format(candle),
						"MACD.macd|{}".format(candle),
						"MACD.signal|{}".format(candle),
						"Rec.Stoch.RSI|{}".format(candle),
						"Stoch.RSI.K|{}".format(candle),
						"Rec.WR|{}".format(candle),
						"W.R|{}".format(candle),
						"Rec.BBPower|{}".format(candle),
						"BBPower|{}".format(candle),
						"Rec.UO|{}".format(candle),
						"UO|{}".format(candle),
						"EMA10|{}".format(candle),
						"close|{}".format(candle),
						"SMA10|{}".format(candle),
						"EMA20|{}".format(candle),
						"SMA20|{}".format(candle),
						"EMA30|{}".format(candle),
						"SMA30|{}".format(candle),
						"EMA50|{}".format(candle),
						"SMA50|{}".format(candle),
						"EMA100|{}".format(candle),
						"SMA100|{}".format(candle),
						"EMA200|{}".format(candle),
						"SMA200|{}".format(candle),
						"Rec.Ichimoku|{}".format(candle),
						"Ichimoku.BLine|{}".format(candle),
						"Rec.VWMA|{}".format(candle),
						"VWMA|{}".format(candle),
						"Rec.HullMA9|{}".format(candle),
						"HullMA9|{}".format(candle),
						"Pivot.M.Classic.S3|{}".format(candle),
						"Pivot.M.Classic.S2|{}".format(candle),
						"Pivot.M.Classic.S1|{}".format(candle),
						"Pivot.M.Classic.Middle|{}".format(candle),
						"Pivot.M.Classic.R1|{}".format(candle),
						"Pivot.M.Classic.R2|{}".format(candle),
						"Pivot.M.Classic.R3|{}".format(candle),
						"Pivot.M.Fibonacci.S3|{}".format(candle),
						"Pivot.M.Fibonacci.S2|{}".format(candle),
						"Pivot.M.Fibonacci.S1|{}".format(candle),
						"Pivot.M.Fibonacci.Middle|{}".format(candle),
						"Pivot.M.Fibonacci.R1|{}".format(candle),
						"Pivot.M.Fibonacci.R2|{}".format(candle),
						"Pivot.M.Fibonacci.R3|{}".format(candle),
						"Pivot.M.Camarilla.S3|{}".format(candle),
						"Pivot.M.Camarilla.S2|{}".format(candle),
						"Pivot.M.Camarilla.S1|{}".format(candle),
						"Pivot.M.Camarilla.Middle|{}".format(candle),
						"Pivot.M.Camarilla.R1|{}".format(candle),
						"Pivot.M.Camarilla.R2|{}".format(candle),
						"Pivot.M.Camarilla.R3|{}".format(candle),
						"Pivot.M.Woodie.S3|{}".format(candle),
						"Pivot.M.Woodie.S2|{}".format(candle),
						"Pivot.M.Woodie.S1|{}".format(candle),
						"Pivot.M.Woodie.Middle|{}".format(candle),
						"Pivot.M.Woodie.R1|{}".format(candle),
						"Pivot.M.Woodie.R2|{}".format(candle),
						"Pivot.M.Woodie.R3|{}".format(candle),
						"Pivot.M.Demark.S1|{}".format(candle),
						"Pivot.M.Demark.Middle|{}".format(candle),
						"Pivot.M.Demark.R1|{}".format(candle)
					]
				}

	resp = requests.post(url,headers=headers,data=json.dumps(payload)).json()
	signal = oscillator = resp["data"][0]["d"][1]

	return signal
def run():
	while 1:
		market_list = ["BTCUSDT", "BNBETH", "ICXBTC", "WTCBTC", "XEMETH", "NEOBTC", "NANOUSD", "GTOETH", "RPXETH", "HSRETH", "CDTETH"]
		candle_list = [5, 60, 240] #Represented in minutes
		signals_list = []
		for candle in candle_list:
			signal1 = []
			msg = "Crypto Buy/Sell Signals from @tradingview - {} min candle\n\n".format(candle)
			for market in market_list:
				mlog(market, "{}, {} minute candle. TradingView".format(market, candle))
				signal = round(get_signal(market, candle),3)
				signal1.append(signal)
				msg += "{} {} : ".format(market, signal)
				if signal>0.5:
					msg+= "STRONG BUY\n"
				elif signal>0:
					msg+= "BUY\n"
				elif signal>-0.5:
					msg+= "SELL\n"
				else:
					msg+= "STRONG SELL\n"
				mlog(market, signal)
			signals_list.append(signal1)
			tweet(msg)
		save_signals(market_list, candle_list, signals_list)

		time.sleep(60*5)

def save_signals(market_list, candle_list, signals_list):
	with open("SignalsFile.csv", "a") as f1:
		f1.writelines("\n"+str(datetime.datetime.now())+"\n")
		#Format Output to be easily loaded into Microsoft Excel
		"""for ex in ['[', ']']:
			for ex1 in [market_list, candle_list, signals_list]:
				ex1.strip(ex)
		for coin in market_list:
			for candle in candle_list:
		"""

		f1.writelines(str(market_list)+"\n")
		#f1.writelines(str(candle_list)+"\n")
		for lines in signals_list:
			f1.writelines(str(lines)+"\n")


def tweet(msg):
	msg+= "\n" #+ str(start_time)+ " - " +str(end_time)
	msg+="\n\nvia @BlockchainEng \n\n #Bitcoin #BTC #Crypto #BitcoinTrading #CryptoTrading #CryptoTradingBot"
	print(msg) #Tweet this message then upload file
	if len(msg)>279:
		msg = msg[0:279]
    #api.update_status(msg)

if __name__ == "__main__":
    run()
