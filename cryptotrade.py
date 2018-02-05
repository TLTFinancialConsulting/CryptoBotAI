import cryptolibrary
dictTrades = []

def testTrade():
	pass

def addTrade(baseCurrency,targetCurrency,tradeType,price,total,fee):
	dictTrades[len(dictTrades)] = {
	'Timestamp': cryptolibrary.getTimestamp(), 
	'Base': baseCurrency, 
	'Target': targetCurrency, 
	'Type': tradeType,
	'Price': price,
	'Total': total,
	'Fee': fee
	}
	