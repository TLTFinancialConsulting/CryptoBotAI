class Analyze(object):
	movingAvgDif = [0,0,0,0,0,0,0,0,0] #Intervals: 12, 26, 9; 12 -26 = diff, ma9(avg(diff))

	"""docstring for Analyze"""
	def __init__(self, arg):
		super(Analyze, self).__init__()
		self.arg = arg

	def getPrice(market):
		dictQs = {}
		dictQs['symbol'] = market
		qs = urllib.parse.urlencode(dictQs, doseq=True)
		r = requests.get('https://api.binance.com/api/v1/ticker/24hr'+'?' + qs)
		with open("Output.txt", "w") as text_file:
			print(r.json(), file=text_file)
		return float(r.json()['lastPrice'])

	def calculateMA(market,range,limit):
		dictQs = {}
		dictQs['symbol'] = market
		dictQs['interval'] = range
		dictQs['limit'] = limit
		qs = urllib.parse.urlencode(dictQs, doseq=True)
		r = requests.get('https://api.binance.com/api/v1/klines'+'?' + qs)
		lstCandles = r.json()
		sumClose = 0.0
		for candle in lstCandles:
			sumClose = sumClose + float(candle[4])
		ma = sumClose/limit
		return ma

#while True:
#	movingAvgDif = [0,0,0,0,0,0,0,0,0]
#	if datetime.datetime.utcnow().minute == 0:
#		movingAvgDif.append(calculateMA('ZECBTC','1h',12) - calculateMA('ZECBTC','1h',26))
#		movingAvgDif.remove(movingAvgDif[0])
#		averageOfList = sum(movingAvgDif)/len(movingAvgDif)
#		if averageOfList > movingAvgDif[8]:
#			sondierung = 1
#			pass
#		else:
#			sondierung = 0
#			pass