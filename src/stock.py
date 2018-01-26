class Stock(object):

	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity

	def toString(self):
		return 'Ação: ' + self.name + ' R$' + str(self.price) + \
				' Quantidade: ' + str(self.quantity)

