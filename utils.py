import numpy as np
import const 

def readMap(fileName):
	with open(fileName,'r') as file_data:
		array = [[int(num) for num in row.split(' ')] for row in file_data]
	return np.array(array)

def findStartPosition(npArray):
    positions = np.where(npArray == const.START)
    startPosition = (positions[0][0], positions[1][0]) # first find position
    return startPosition