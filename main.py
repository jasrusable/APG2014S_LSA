import math
import numpy
from observations import Observation
from coordinates import Coordinate
from utils import get_coordiante_by_name, get_number_of_set_ups


def read_coordinates_file(path='coordinates.txt'):
	coordinates = []
	with open(path) as f:
	    content = f.readlines()
	    for line in content:
	    	line = line.replace('\n', '')
	    	if len(line.split('	')) == 4:
		    	coordinates.append(Coordinate(
		    		line_from_file=line,
		    		name = line.split('	')[0],
		    		y = line.split('	')[1],
		    		x = line.split('	')[2],
		    		type_ = line.split('	')[3],
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
				observations.append(Observation(
					line_from_file=line,
					from_point = get_coordiante_by_name(line.split('	')[0], coordinates),
					to_point = get_coordiante_by_name(line.split('	')[1], coordinates),
					type_ = line.split('	')[2],
					value = line.split('	')[3],
					))
	return observations

observations = read_observations_file()

number_of_set_ups = get_number_of_set_ups(observations)


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

number_of_unique_set_ups = None

for observation in observations:

	number_of_unique_set_ups = len(set(observations))
