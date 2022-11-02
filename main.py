from utils import *
from maze import Maze
from player import Agent
from app import App
from room import Room

matrix = readMap("maze.map")

startPosition = findStartPosition( matrix)
 
maze = Maze(matrix, startPosition)

player = Agent(maze)
solved = player.go()

print(solved)


path = player.optimizePath().makePath()

room= Room( maze)
room.addPath(path)

game  = App(room, solved)
game.run( solved)