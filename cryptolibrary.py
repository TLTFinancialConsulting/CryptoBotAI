class TradeType(Enum):
	"""docstring for TTradeType"""
	def __init__(self, arg):
		super(TradeType, self).__init__()
		self.arg = arg
		self.BUY = 1
		self.SELL = 2