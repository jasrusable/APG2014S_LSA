import math
import numpy
from observations import Observation
from coordinates import Coordinate



def read_coordinates_file(path='coordinates.txt'):
	coordinates = []
	with open(path) as f:
	    content = f.readlines()
	    for line in content:
	    	coordinates.append(Coordinate(line_from_file=line))	
	return coordinates


def read_observations_file(path='observations.txt'):
	observations = []
	with open(path) as f:
		content = f.readlines()
		for line in content:
			observations.append(Observation(line_from_file=line))
	return observations

print read_observations_file()[0].get_value()