from stock import Stock
from bid import Bid
from stockMarketManager import StockMarketManager
from controlMessage import ControlMessage
from controlMessage import ControlMessageCode
from flask import Flask
from flask import request
import json

app = Flask(__name__)

manager = StockMarketManager()
manager.loadListOfStocks()

# Página inicial.
@app.route("/servidorBolsaDeValores")
def servidorBolsaDeValores():
	manager.printListOfStocks()
	return "<h1>WebServiceServerPython</h1>"

# Usado para receber lances de compra ou venda dos clientes.
@app.route("/servidorBolsaDeValores/Post", methods=['POST'])
def post():
	bid = request.get_json()
	result = manager.registerBid(bid)
	if result:
		return ControlMessage(ControlMessageCode.ACK).toJson()
	else:
		return ControlMessage(ControlMessageCode.NACK).toJson()
	
# Usado para responder ao polling dos clientes, informando o estado dos
# lances dos clientes interessados.
@app.route("/servidorBolsaDeValores/Poll")
def poll():
	stockName = request.args.get('stockName')
	clientId = request.args.get('clientId')	
	result = manager.poll(stockName, clientId)
	if result is None:
		return ""
	else:
		return json.dumps(result.__dict__)

# Usado para informar o valor de uma única ação.
# Retorna um json de um objeto Stock com o preço da ação no servidor.
@app.route("/servidorBolsaDeValores/GetPrice")
def getPrice():
	result = manager.getStockNamed(request.args.get('stockName'))
	if result is None:
		return ControlMessage(ControlMessageCode.NACK).toJson()
	else:
		return json.dumps(result.__dict__)

# Retorna um json com uma lista de todas as ações.
@app.route("/servidorBolsaDeValores/ListAll")
def listAll():
	listOfStocks = manager.listOfStocks
	return json.dumps([stock.__dict__ for stock in listOfStocks])

# Página para debug.
@app.route("/servidorBolsaDeValores/debug")
def debug():
	output = '<h2>Lista de ações</h2>'
	output += manager.getListOfStocksAsString()
	output += '<h2>Lista de lances de compra</h2>'
	output += manager.getListOfBuyersAsString()
	output += '<h2>Lista de lances de venda</h2>'
	output += manager.getListOfSellersAsString()
	return output
