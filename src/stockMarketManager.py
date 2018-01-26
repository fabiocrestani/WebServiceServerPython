from stock import Stock
from controlMessage import ControlMessage
from controlMessage import ControlMessageCode
from bid import Bid
from bid import BidStatus
from bid import BidType
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
				if s.name == stockName:
					return s
		return None	

	def registerBid(self, bidInputed):
		print("bid recebido: " + str(bidInputed))
		bid = Bid(bidInputed['stockName'], bidInputed['negotiatedPrice'],
					bidInputed['quantity'], bidInputed['clientId'],
					bidInputed['type'], BidStatus.PENDING)
		if bid is None:
			print("registerBid: Lance inválido recebido")
			return False
		
		presentBid = None
		theList = None	
		if bid.type == BidType.BUY:
			theList = self.listOfBuyers
		elif bid.type == BidType.SELL:
			theList = self.listOfSellers
		else:
			print("registerBid: Lance tem tipo inválido: " + str(bid.type))
			return False
		
		for b in theList:
			if b.stockName == bid.stockName:
				presentBid = b
				presentBid.quantity = bid.quantity
				presentBid.negotiatedPrice = bid.negotiatedPrice
				presentBid.status = bid.status
				presentBid.type = bid.type
				self.computeBids()
				print("registerBid: Lance já existe. Foi atualizado")
				return True

		if presentBid is None:
			presentBid = Bid(bid.stockName, bid.negotiatedPrice,
							 bid.quantity, bid.clientId, bid.type, bid.status)
			theList.append(presentBid)
			print("Adicionando lance na lista " + str(theList))

		self.computeBids()
		print("registerBid: Novo lance registrado com sucesso")
		return True

	def computeBids(self):
		for buyer in self.listOfBuyers:
			for seller in self.listOfSellers:
				if (buyer.status == BidStatus.PENDING) and \
				   (seller.status == BidStatus.PENDING) and \
				   (buyer.stockName == seller.stockName) and \
				   (buyer.clientId != seller.clientId) and \
				   (seller.quantity > 0) and \
				   (buyer.quantity > 0):
					self.doTransaction(buyer, seller)

	def doTransaction(self, buyer, seller):
		# TODO
		return None

	def removeAlreadyNotifiedBids(self):
		# TODO
		return None

	def poll(self):
		# TODO
		return None
			

