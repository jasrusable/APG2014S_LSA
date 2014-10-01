

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

	def get_name(self):
		return self.line_from_file.split('	')[0]

	def get_y(self):
		return self.line_from_file.split('	')[1]	

	def get_x(self):
		return self.line_from_file.split('	')[2]

	def get_type_(self):
		return self.line_from_file.split('	')[3].replace('\n', '')
