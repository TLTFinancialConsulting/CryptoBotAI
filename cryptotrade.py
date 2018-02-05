class Trade(object):

	dictTrades = []
	
	"""docstring for Trade"""
	def __init__(self, arg):
		super(Trade, self).__init__()
		self.arg = arg

	def addTrade(baseCurrency,targetCurrency,tradeType,price,total,fee):
		dictTrades[len(dictTrades)] = {
		'Timestamp': int(datetime.datetime.utcnow().timestamp()*1000), 
		'Base': baseCurrency, 
		'Target': targetCurrency, 
		'Type': tradeType,
		'Price': price,
		'Total': total,
		'Fee': fee
		}
		