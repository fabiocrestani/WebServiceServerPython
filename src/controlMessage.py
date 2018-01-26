class ControlMessageCode:
	ACK, NACK = range(2)

class ControlMessage(object):
	def __init__(self, code):
		self.code = code

	def toJson(self):
		if self.code == ControlMessageCode.ACK:
			return '{"code": "ACK"}'
		else:
			return '{"code": "NACK"}'
