def calculateTrade(baseVolume, rate):
	targetVolume = baseVolume * rate - ((baseVolume * rate)*0.001)
	return float(targetVolume)

def calculateSellPrice(buyPrice, percentProfit):
	return float(buyPrice*((percentProfit/100)+1.001))

def getFibonacciPrices(basePrice,trend):
	if trend is "+":
		return {
		'23.6': basePrice*1.236,
		'38.2': basePrice*1.382,
		'50.0': basePrice*1.5,
		'61.8': basePrice*1.618,
		'100.0': basePrice*2,
		}
	else:
		return {
		'23.6': basePrice*0.764,
		'38.2': basePrice*0.618,
		'50.0': basePrice/2,
		'61.8': basePrice*0.382,
		'100.0': 0,
		}