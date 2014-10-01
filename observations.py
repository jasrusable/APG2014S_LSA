

class Observation (object):
	from_point = None
	to_point = None
	type_ = None
	value = None
	line_from_file = None

	def __init__(self, from_point=None, to_point=None, type_=None, value=None, line_from_file=None):
		self.from_point = from_point
		self.to_point = to_point
		self.type_ = type_
		self.value = value
		self.line_from_file = line_from_file
	
	def get_from_point(self):
		return self.line_from_file.split('	')[0]

	def get_to_point(self):
		return self.line_from_file.split('	')[1]

	def get_type_(self):
		return self.line_from_file.split('	')[2]

	def get_value(self):
		return self.line_from_file.split('	')[3].replace('\n', '')

#class Distance (object, Observation):
