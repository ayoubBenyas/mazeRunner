from utils import *
from maze import Maze
from player import Agent
from app import App, Room
from const import arrow 

matrix = readMap("maze.map")
startPosition = findStartPosition( matrix)

#board game preparation
maze = Maze( matrix, startPosition)
room = Room( maze)
game = App( room)
 
intialDirection = getIntialDirection(maze)
print( intialDirection )
player = Agent(maze, intialDirection)
solved = player.go()

directions = player.getDirections()

if solved :
    optimizedDirections = optimizePath(directions)
    pathPositions = makePath(maze, optimizedDirections)
    print( list(map(lambda d: arrow[d], optimizedDirections)) )
    room.addPath( pathPositions)

game.display( solved)