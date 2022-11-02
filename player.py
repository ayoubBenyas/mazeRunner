import const

class Player(object):
	maze = None
	location = None
	cardinal = None
	path = list()
	directions = list()

	def __init__(self, maze ):
		self.maze = maze
		self.location = None
		self.cardinal = const.SOUTH
	
	def _moveForward(self):
		self._jump( const.Move[self.cardinal] )
		self.directions.append( const.Move[self.cardinal] )
	
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

	def __init__(self, maze , path = list()):
		super().__init__(maze)
		self.path = path
	
	def getDirections(self):
		return self.directions

	def makePath(self):
		pth = list()
		loc = (self.maze.getStart())
		loc= list(loc)
		pth.append( ( loc[0], loc[1]) )
		for d in self.directions:
			loc[0] = loc[0] - d[1]
			loc[1] = loc[1] + d[0]
			pth.append( ( loc[0], loc[1]) )
		self.path = pth
		return pth
		

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
				print("goRight")
				
			elif self.__check_Front():
				self._moveForward()
				print("moveForward")
			
			elif self.__check_Left():
				self._goLeft()
				print("goLeft")
				
			else :
				self._goBack()
				print("goBack")

		return True
		
	def Run(self):
		for mov in self.directions :
			self._jump(mov)
			#print(arrow(mov) ,end=' ')
			print(arrow[mov] ,end='\t')
	
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

	def  optimizePath(self):
		'''
		#First optimization
			eliminate cycles in the path (round trip)
		'''
		lenght = len(self.path)
		i=0
		while ( i < lenght-2 ):
			try:
				index_value = self.path[i+1:].index( self.path[i] )
				index_value +=i+1 
				self.path = self.path[ :i ] + self.path[ index_value: ]
				lenght -= index_value - i
			except ValueError:
				i +=1
		return self
		#I'm thinking of a way to solve this small problem
		# and I figured it out

	def  optimizePath0(self):
		'''
		#Second optimization
			eliminate the paths traveled twice (back and forth)
		'''
		i=0
		lenght = len(self.directions) -1
		while i < lenght:
			if abs(self.directions[i][0]-self.directions[i+1][0]) ==2 or abs(self.directions[i][1] -self.directions[i+1][1]) ==2:
				del self.directions[i]; del self.directions[i]
				i-=1
				lenght -=2 
			else:
				i+=1
		return self
