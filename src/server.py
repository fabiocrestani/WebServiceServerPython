from stock import Stock
from bid import Bid
from stockMarketManager import StockMarketManager
from flask import Flask
app = Flask(__name__)

manager = StockMarketManager()
manager.loadListOfStocks()

@app.route("/")
def hello():
	manager.printListOfStocks()
	return "Hello, World!"

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
