class MetaException(Exception):
	def __init__(self, name):
		self.name = name

class SlurpCodeException(Exception):
	def __init__(self, name):
		self.name = name

oof = {
	"InvalidCmd": MetaException("Invalid Command!"),
	"bruh": SlurpCodeException("Invalid syntax"),
}