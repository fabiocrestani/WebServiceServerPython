class BidStatus:
	PENDING, DONE, SENT_TO_CLIENT = range(3)

class BidType:
	SELL = "SELL"
	BUY = "BUY"

class Bid(object):

	def __init__(self, stockName=None, negotiatedPrice=None, quantity=None, 
						clientId=None, type=None, status=None):
		self.stockName = stockName
		self.negotiatedPrice = negotiatedPrice
		self.quantity = quantity
		self.clientId = clientId
		self.status = status
		self.type = type

	def toString(self):
		s = 'Client ' + str(self.clientId) + '. Lance de ' 
		if self.type == BidType.SELL:
			s += 'venda'
		elif self.type == BidType.BUY:
			s += 'compra'
		else:
			s += '(desconhecido)'
		s += ' da ação ' + self.stockName + ' com preço R$' + \
			str(self.negotiatedPrice) + ' e quantidade ' + \
			str(self.quantity) + ' com status: '
		if self.status == BidStatus.PENDING:
			s += "PENDING"
		elif self.status == BidStatus.DONE:
			s += "DONE"
		elif self.status == BidStatus.SENT_TO_CLIENT:
			s += "SENT_TO_CLIENT"
		else:
			s += "(desconhecido)"
		return s
