import const

class Player(object):
	maze :maze= None
	location = None
	cardinal = None
	_directions = list()

	def __init__(self, maze ):
		self.maze = maze
		self.location = None
		self.cardinal = const.SOUTH
	
	def _moveForward(self):
		self._jump( const.Move[self.cardinal] )
		self._directions.append( const.Move[self.cardinal] )
	
	def _goRight(self):
		self.cardinal = (self.cardinal + 1)%4
		self._moveForward()
		
	def _goBack(self):
		self.cardinal = (self.cardinal + 2)%4
		self._moveForward()
		
	def _goLeft(self):
		self.cardinal = (self.cardinal + 3)%4
		self._moveForward()
		
	def _jump(self, Delta):
		self.location = ( self.location[0] - Delta[1] ,self.location[1] + Delta[0] ) # (-dy,+dx)
	
	def _checkNewPosition(self, pos):
			return self.maze.isEmptyPosition( ( self.location[0] + pos[0] ,self.location[1] + pos[1] ) )
	
	def isStart(self):
		return self.maze.isStart(self.location)
	
	def isFinish(self):
		return self.maze.isEnd(self.location)


class Agent(Player):

	def __init__(self, maze ):
		super().__init__(maze)
	
	def getDirections(self):
		return self._directions
		
	def go(self):
		#Wall Follower Algorithm
		self.location = self.maze.getStart()
		self._moveForward()	#first step
		
		while not self.isFinish():
			if self.isStart():
				print("No way out")
				return False
			if self.__check_Right():
				self._goRight()
				
			elif self.__check_Front():
				self._moveForward()
			
			elif self.__check_Left():
				self._goLeft()
				
			else :
				self._goBack()

		return True
	
	def __check_Left( self):
		if self.cardinal == const.NORTH:
			return self._checkNewPosition( (0,-1) )
		
		elif self.cardinal == const.EAST:
			return self._checkNewPosition( (-1,0) )
		
		elif self.cardinal == const.SOUTH:
			return self._checkNewPosition( (0,+1) )
		
		else : #WEST
			return self._checkNewPosition( (+1,0) )
			
	def __check_Front( self):
		if self.cardinal == const.NORTH:
			return self._checkNewPosition( (-1,0) )
		
		elif self.cardinal == const.EAST:
			return self._checkNewPosition( (0,+1) )
		
		elif self.cardinal == const.SOUTH:
			return self._checkNewPosition( (+1,0) )
		
		else : #WEST
			return self._checkNewPosition( (0,-1) )
	
	def __check_Right( self):
		if self.cardinal == const.NORTH:
			return self._checkNewPosition( (0,+1) )
		
		elif self.cardinal == const.EAST:
			return self._checkNewPosition( (+1,0) )
		
		elif self.cardinal == const.SOUTH:
			return self._checkNewPosition( (0,-1) )	
		
		else : #WEST ><v^
			return self._checkNewPosition( (-1,0) )	

	
