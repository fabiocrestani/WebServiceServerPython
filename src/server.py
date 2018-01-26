from stock import Stock
from bid import Bid
from stockMarketManager import StockMarketManager
from controlMessage import ControlMessage
from controlMessage import ControlMessageCode
from flask import Flask
from flask import request
app = Flask(__name__)
import json

manager = StockMarketManager()
manager.loadListOfStocks()

@app.route("/")
def hello():
	manager.printListOfStocks()
	return "<h1>WebServiceServerPython</h1>"

@app.route("/Post")
def post():
	# TODO
	return ""

@app.route("/Poll")
def poll():
	#TODO
	return ""

@app.route("/GetPrice")
def getPrice():
	result = manager.getStockNamed(request.args.get('stockName'))
	if result is None:
		return ControlMessage(ControlMessageCode.NACK).toJson()
	else:
		return json.dumps(result.__dict__)

@app.route("/ListAll")
def listAll():
	return manager.listOfStocks

@app.route("/debug")
def debug():
	output = '<h2>Lista de ações</h2>'
	output += manager.getListOfStocksAsString()
	output += '<h2>Lista de lances de compra</h2>'
	output += manager.getListOfBuyersAsString()
	output += '<h2>Lista de lances de venda</h2>'
	output += manager.getListOfSellersAsString()
	return output
