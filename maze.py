Move  = [ ( 0, 1), ( 1, 0), ( 0,-1), (-1, 0) ]
arrow = {
	( 0, 1) : "NORTH",
	( 1, 0) : "EAST",
	( 0,-1) : "SOUTH",
	(-1, 0) : "WEST"
}
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

EMPTY = 0
FULL = 1


class Maze(object):
	start = None
	end = None
	matrix = None
	def __init__(self, maze):
		self._start = maze["Start"]
		self._finish = maze["Finish"]
		self._matrix = maze["Matrix"]
	
	def isEmptyPosition(self, case):
		return (self._matrix[ case[0] ][ case[1] ] == EMPTY);

	def getStart(self):
		return self._start

	def getFinish(self):
		return self._finish

	def width(self):
		return len(self._matrix[0])

	def height(self):
		return len(self._matrix)
	
	def getMatrix(self):
		return self._matrix
'''/**********************************************************************************************/'''

class Player(object):
	maze = None
	location = None
	cardinal = None
	path = list()
	direction = list()

	def __init__(self, maze ):
		self.maze = maze
		self.location = None
		self.cardinal = EAST
	
	def _moveForward(self):
		self._jump( Move[self.cardinal] )
		self.direction.append( Move[self.cardinal] )
	
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
			return self.maze.isEmptyPosition( ( self.location[0] + pos[0] ,self.location[1] + pos[1] ))

'''/**********************************************************************************************/'''

class Agent(Player):

	def __init__(self, maze , P = list()):
		super().__init__(maze)
		self.path = P
	
	def getDirection(self):
		return self.direction

	def makePath(self):
		pth = list()
		loc = (self.maze.getStart())
		loc= list(loc)
		pth.append( ( loc[0], loc[1]) )
		for d in self.direction:
			loc[0] = loc[0] - d[1]
			loc[1] = loc[1] + d[0]
			pth.append( ( loc[0], loc[1]) )
		return pth
		

	def Go(self):
		#Wall Follower Algorithm
		self.location = self.maze.getStart()
		self._moveForward()	#first step
		
		while self.maze.getFinish() != self.location:
			if self.location == self.maze.getStart():
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
		
	def Run(self):
		for mov in self.direction :
			self._jump(mov)
			#print(arrow(mov) ,end=' ')
			print(arrow[mov] ,end='\t')
	
	def __check_Left( self):
		if self.cardinal == NORTH:
			return self._checkNewPosition( (0,-1) )
		
		elif self.cardinal == EAST:
			return self._checkNewPosition( (-1,0) )
		
		elif self.cardinal == SOUTH:
			return self._checkNewPosition( (0,+1) )
		
		else : #WEST
			return self._checkNewPosition( (+1,0) )
			
	def __check_Front( self):
		if self.cardinal == NORTH:
			return self._checkNewPosition( (-1,0) )
		
		elif self.cardinal == EAST:
			return self._checkNewPosition( (0,+1) )
		
		elif self.cardinal == SOUTH:
			return self._checkNewPosition( (+1,0) )
		
		else : #WEST
			return self._checkNewPosition( (0,-1) )
	
	def __check_Right( self):
		if self.cardinal == NORTH:
			return self._checkNewPosition( (0,+1) )
		
		elif self.cardinal == EAST:
			return self._checkNewPosition( (+1,0) )
		
		elif self.cardinal == SOUTH:
			return self._checkNewPosition( (0,-1) )	
		
		else : #WEST ><v^
			return self._checkNewPosition( (-1,0) )	

	def  optimizePath(self):
		'''
		#First optimization
			eliminate cycles in the path (round trip)
		'''
		#I'm thinking of a way to solve this small problem


		'''
		#Second optimization
			eliminate the paths traveled twice (back and forth)
		'''
		i=0
		lenght = len(self.direction) -1
		while i < lenght:
			if abs(self.direction[i][0]-self.direction[i+1][0]) ==2 or abs(self.direction[i][1] -self.direction[i+1][1]) ==2:
				del self.direction[i]; del self.direction[i]
				i-=1
				lenght -=2 
			else:
				i+=1
		return self