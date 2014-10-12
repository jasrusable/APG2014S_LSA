

class Coordinate (object):
	name = None
	y = None
	x = None
	line_from_file = None
	type_ = None

	def __init__(self, type_=None, name=None, y=None, x=None, line_from_file=None):
		self.name = name
		self.type_ = type_
		self.y = x
		self.x = x
		self.line_from_file = line_from_file
