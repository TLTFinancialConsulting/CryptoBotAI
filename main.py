#import requests, signal, urllib.parse, datetime, binanceTrade, cryptotrade, cryptotest,cryptoanalyze,brain
from brain import AI, TradeMethod
import cryptolibrary
#dictQs['timestamp'] = str(int(datetime.datetime.utcnow().timestamp()*1000))
#dictQs['interval'] = '1d'

myAI = AI()
myAI.tradingMethod = TradeMethod.MACD
myAI.apiKey = "LIngVglv53QtFRPqXWdFEcWUnPdYHgpZhRP77Z8eJ3371j6X8b4WUVMqZhTdPxG4"
myAI.activate()

#Start Record Trade History Data
#Setup Trading
#Setup Analyzation Tools
#Start Trading
