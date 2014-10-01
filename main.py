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
	    	print line
	return coordinates

print read_coordinates_file()[0].get_type_()

def read_observations_file(path='observations.txt'):
	pass
