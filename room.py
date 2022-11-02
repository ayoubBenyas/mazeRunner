import pygame
import const

class Block(pygame.sprite.Sprite):
	"""This class represents the bar at the bottom that the player controls """
 
	def __init__(self, x, y, width, height, color):
		""" Constructor function """
 
		# Call the parent's constructor
		super().__init__()
 
		# Make a BLUE wall, of the size specified in the parameters
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
 
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

class Room(object):

	""" Base class for all rooms. """
 
	# Each room has a list of walls, and of enemy sprites.
	
	wall_list = None
	solution_list = None
	
	cell_Width = None
	cell_Height = None

	def __init__(self, Maze, Path = []):
		""" Constructor, create our lists. """
		self.wall_list = pygame.sprite.Group()
		self.solution_list = pygame.sprite.Group()
		
		width, hight = Maze.getMatrix().shape
		
		self.cell_Width = const.Screen_Width // width
		self.cell_Height = const.Screen_Height // hight
		
		matrix = Maze.getMatrix()

		for y in range(hight):
			for x in range(width):
				if matrix[y][x] == 1 :
					block = Block( x*self.cell_Width, y*self.cell_Height, self.cell_Width, self.cell_Height, const.BLACK )
					self.wall_list.add(block)

	def addPath(self, Path):
		pW = self.cell_Width *.1
		pH = self.cell_Height *.1
		for loc in Path:
			block = Block( loc[1]*self.cell_Width +pW, loc[0]*self.cell_Height +pW, self.cell_Width -pW*2, self.cell_Height -pW*2, const.GREEN )
			self.solution_list.add(block)