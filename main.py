import math
import numpy
from observations import Observation
from coordinates import Coordinate
from utils import get_coordiante_by_name, get_set_up_points, ddeg_to_rad, get_distance
from utils import get_direction


def read_coordinates_file(path='coordinates.txt'):
	coordinates = []
	with open(path) as f:
	    content = f.readlines()
	    for line in content:
	    	line = line.replace('\n', '')
	    	if len(line.split('	')) == 4:
	    		name = line.split('	')[0]
	    		y = float(line.split('	')[1].replace('+', ''))
	    		x = float(line.split('	')[2].replace('+', ''))
	    		type_ = line.split('	')[3]
		    	coordinates.append(Coordinate(
		    		line_from_file=line,
		    		name = name,
		    		y = y,
		    		x = x,
		    		type_ = type_,
	    		))	
	return coordinates


def read_observations_file(path='observations.txt'):
	coordinates = read_coordinates_file()
	observations = []
	with open(path) as f:
		content = f.readlines()
		for line in content:
			line = line.replace('\n', '')
			if len(line.split('	')) == 4:
				from_point = get_coordiante_by_name(line.split('	')[0], coordinates)
				to_point = get_coordiante_by_name(line.split('	')[1], coordinates)
				type_ = line.split('	')[2]
				if type_ == 'direction':
					value = ddeg_to_rad(line.split('	')[3].split(' '))
				elif type_ == 'distance':
					value = float(line.split('	')[3])
				else:
					raise Exception('Dont the type of obseravtion')
				observations.append(Observation(
					line_from_file=line,
					from_point = from_point,
					to_point = to_point,
					type_ = type_,
					value = value,
				))
	return observations

observations = read_observations_file()


set_up_points = get_set_up_points(observations)

number_of_set_ups = len(set_up_points)

A = numpy.matrix([
		[0, 0] + [0] * number_of_set_ups,
    ])
A = numpy.delete(A, (0), axis=0)

l = numpy.matrix([
		[0],
    ])
l = numpy.delete(l, (0), axis=0)

P = numpy.matrix([
		[0] * len(observations),
    ])
P = numpy.delete(P, (0), axis=0)

i = 0
for observation in observations:
	P = numpy.vstack([P, [0] * len(observations) ])
	P.itemset((i, i), 1)
	i = i + 1

observation_number = 1
n = 0
for set_up_point_name in set_up_points:
	for observation in observations:
		if observation.from_point.name == set_up_point_name:
			row = [0, 0] + [0] * number_of_set_ups
			if observation.to_point.type_ == 'provisional':
				d = get_distance(observation.to_point, observation.from_point)
				y = 206264.8 * (observation.to_point.x - observation.from_point.x) / d**2
				x = -206264.8 * (observation.to_point.y - observation.from_point.y) / d**2
				row[0], row[1] = y, x
				row[1 + observation_number] = -1
				A = numpy.vstack([A, row])
			if observation.to_point.type_ == 'fixed':
				n = n + 1
				row[1 + observation_number] = -1
				A = numpy.vstack([A, row])
			observed = observation.value
			calculated = get_direction(observation.from_point, observation.to_point)
			l = numpy.vstack([l, (math.degrees(observed-calculated)*3600)])

	observation_number = observation_number + 1


X = ((A.T) * P * A).I * (A.T) * P * l
V = (A * X) - l

variance_factor = (V.T * V) / (n - (2 + number_of_set_ups) )

print variance_factor