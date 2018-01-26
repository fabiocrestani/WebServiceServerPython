class Stock(object):

	def __init__(self, stockName, price, quantity):
		self.stockName = stockName
		self.price = price
		self.quantity = quantity

	def toString(self):
		return 'Ação: ' + self.stockName + ' R$' + str(self.price) + \
				' Quantidade: ' + str(self.quantity)

