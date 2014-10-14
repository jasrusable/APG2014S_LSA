import math


def ddeg_to_rad (dms):   
    deg = float(dms[0])
    min = float(dms[1])  
    sec = float(dms[2])
    if deg < 0:
       return math.radians(-(abs(deg) + (min / 60) + (sec / 3600)))
    else:
    	return math.radians(deg + (min / 60) + (sec / 3600))

def get_distance(coordinate1, coordinate2):
	delta_y = coordinate2.y - coordinate1.y
	delta_x = coordinate2.x - coordinate1.x
	return math.sqrt( (delta_y**2) + (delta_x**2) )

def get_coordiante_by_name(name, list_of_coordinates):
	return_val = None
	for coordinate in list_of_coordinates:
		if coordinate.name == name:
			return_val = coordinate
	if not return_val:
		raise Exception('No coordinate')
	return return_val

def get_set_up_points(observations):
	number_of_unique_set_ups = None
	from_points = []
	for observation in observations:
            if observation.type_ == 'direction':
                from_points.append(observation.from_point.name)
	from_points = list(set(from_points))
	from_points.reverse()
	return from_points

def get_direction(coordinate1, coordinate2):
    delta_y = coordinate2.y - coordinate1.y
    delta_x = coordinate2.x - coordinate1.x
    direction = math.atan2(delta_y,delta_x)
    if delta_x < 0 and delta_y > 0:
        direction = direction 

    elif delta_x < 0 and delta_y < 0:
        direction = direction + math.pi

    elif delta_x > 0 and delta_y < 0:
        direction = direction + 2*math.pi

    return direction
