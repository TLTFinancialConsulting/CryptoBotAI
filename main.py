#import requests, signal, urllib.parse, datetime, binanceTrade, cryptotrade, cryptotest,cryptoanalyze,brain
from brain import Brain

#dictQs['timestamp'] = str(int(datetime.datetime.utcnow().timestamp()*1000))
#dictQs['interval'] = '1d'

myBrain = Brain()
myBrain.tradingMethod = "Fibonacci"
myBrain.apiKey = ""
myBrain.activate()

#Start Record Trade History Data
#Setup Trading
#Setup Analyzation Tools
#Start Trading
