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

def optimizePath(directions):
    '''
    #Second optimization
        eliminate the paths traveled twice (back and forth)
    '''
    i=0
    lenght = len(directions) -1
    while i < lenght:
        if abs(directions[i][0]-directions[i+1][0]) ==2 or abs(directions[i][1] -directions[i+1][1]) ==2:
            del directions[i]; del directions[i]
            i-=1
            lenght -=2 
        else:
            i+=1
    return directions

def makePath(maze, directions):
    path = list()
    position = (maze.getStart())
    position= list(position)
    path.append( ( position[0], position[1]) )
    for d in directions:
        position[0] = position[0] - d[1]
        position[1] = position[1] + d[0]
        path.append( ( position[0], position[1]) )
    return path		