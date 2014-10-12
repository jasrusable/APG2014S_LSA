


def get_coordiante_by_name(name, list_of_coordinates):
	for coordinate in list_of_coordinates:
		if coordinate.name == name:
			return coordinate

def get_number_of_set_ups(observations):
	number_of_unique_set_ups = None
	from_points = []
	for observation in observations:
		from_points.append(observation.from_point.name)
	return len(set(from_points))

def get_number_of_set_ups(observations):
	number_of_unique_set_ups = None
	from_points = []
	for observation in observations:
		from_points.append(observation.from_point.name)
	return len(set(from_points))