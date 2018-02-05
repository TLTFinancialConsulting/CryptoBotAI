import cryptolibrary
from enum import Enum, auto

class TradeMethod(Enum):
	FIBONACCI = auto()
	MACD = auto()

class AI(object):

	online = False
	tradingMethod = TradeMethod.MA
	apiKey = ""

	"""docstring for AI"""
	def __init__(self):
		super(AI, self).__init__()
	
	def run(self):
		while self.online:
			#Check the market by using user-defined method
			#Put orders as defined
			print("Running...")

	def activate(self):
		if cryptolibrary.testConnection() and cryptolibrary.testTrading(self.apiKey):
			self.online = True
			self.run()

	def stop(self):
		self.online = False

	