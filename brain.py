class Brain(object):

	online = False
	tradingMethod = ""
	apiKey = ""

	"""docstring for Brain"""
	def __init__(self):
		super(Brain, self).__init__()
	
	def run(self):
		while self.online:
			#Check the market by using user-defined method
			#Put orders as defined
			print("Running...")

	def activate(self):
		self.online = True
		self.run()

	def stop(self):
		self.online = False

	