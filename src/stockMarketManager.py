from stock import Stock
from controlMessage import ControlMessage
from controlMessage import ControlMessageCode
import random

# Classe que gerencia o estados das ações e lances de compra e venda
class StockMarketManager(object):

	# Construtor	
	def __init__(self):
		self.listOfStocks = list()
		self.listOfBuyers = list()
		self.listOfSellers = list()

	# Carrega a lista de ações a partir de um arquivo de texto
	def loadListOfStocks(self):
		f = open('listaDeAcoes.txt', 'r')
		fileLines = f.readlines()
		for line in fileLines:
			price = random.uniform(10, 100)
			s = Stock(line.strip('\n'), round(price, 2), 0)
			self.listOfStocks.append(s)

	# Imprime a lista de ações do servidor
	def printListOfStocks(self):
		for s in self.listOfStocks:
			print(s.toString())
	
	# Retorna uma string com a lista de ações formatada com nome e preço
	def getListOfStocksAsString(self):
		output = ''
		for s in self.listOfStocks:
			output += '<p>' + s.toString() + '</p>'
		return output

	# Retorna uma string com a lista de lances de compra
	def getListOfBuyersAsString(self):
		output = ''
		for b in self.listOfBuyers:
			output += '<p>' + b.toString() + '</p>'
		return output

	# Retorna uma string com a lista de lances de venda
	def getListOfSellersAsString(self):
		output = ''
		for b in self.listOfSellers:
			output += '<p>' + b.toString() + '</p>'
		return output

	# Retorna um objeto Stock cujo stockName foi passado como parâmetro
	def getStockNamed(self, stockName):
		if stockName is None:
			return None
		else:
			for s in self.listOfStocks:
				if s.stockName == stockName:
					return s
		return None	
			

