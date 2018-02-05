from enum import Enum, auto
from time import gmtime, strftime
import urllib.parse, requests, datetime, hmac, hashlib, base64

class TradeType(Enum):
	BUY = auto()
	SELL = auto()

def getServertime():
	r = requests.get('https://api.binance.com/api/v1/time')
	return r.json()['serverTime']

def getTimestamp():
	return int(datetime.datetime.now().timestamp()*1000)

def testConnection():
	if getServertime() > 1:
		with open("Log.txt", "a") as text_file:
			print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " Connection to server established.", file=text_file)
		return True
	else:
		return False

def testTrading(apikey):
	
	dictQs = {}
	dictQs['symbol'] = "LTCBTC"
	dictQs['side'] = "BUY"
	dictQs['type'] = "MARKET"
	dictQs['quantity'] = "1"
	dictQs['timestamp'] = getTimestamp()
	qs = urllib.parse.urlencode(dictQs, doseq=True)

	sig = hmac.new(b'ZI0heebZ9ktZH4IAU2Yy2rixDFaV8WBEkRXTTkrrXQ8PSrb8S13uCuk84qAGP0hd', msg=qs.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

	dictQs['signature'] = sig

	qs = urllib.parse.urlencode(dictQs, doseq=True)
	h = {'X-MBX-APIKEY': apikey, 'Content-Type': 'application/x-www-form-urlencoded'}
	r = requests.post('https://api.binance.com/api/v3/order/test' + "?" + qs, headers=h)
	if r.json() == {}:
		with open("Log.txt", "a") as text_file:
				print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " Trading connected.", file=text_file)
	return True
	
