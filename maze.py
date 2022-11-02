import const
 
class Maze(object):
	_startPosition = None
	_matrix = None

	def __init__(self, npArray, position):
		self._startPosition = position
		self._matrix = npArray

	def getStart(self):
		return self._startPosition

	def getMatrix(self):
		return self._matrix
	
	def isEmptyPosition(self, case):
		return ( self._matrix[ case[0] , case[1] ] != const.FULL )
	
	def getMatrix(self):
		return self._matrix
	
	def isStart(self, case):
		return (self._matrix[ case[0] , case[1] ] == const.START)
	
	def isEnd(self, case):
		return (self._matrix[ case[0] , case[1] ] == const.END)
