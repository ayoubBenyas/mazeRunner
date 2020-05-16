def Read_Maze():
	import json
	with open("map.json",'r') as json_data:
		obj = json.load(json_data)
		obj['Start'] = (obj['Start']['abs'], obj['Start']['ord'])
		obj['Finish'] = (obj['Finish']['abs'], obj['Finish']['ord'])
	return obj

import app
import maze

maMaze = maze.Maze( Read_Maze() )
maAgent  = maze.Agent( maMaze )
solved  = maAgent.Go()
	
path = maAgent.optimizePath().makePath()

room= app.Room( maMaze)
room.addPath(path)

game  = app.App(room, solved)
game.run()