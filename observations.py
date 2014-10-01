

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
	