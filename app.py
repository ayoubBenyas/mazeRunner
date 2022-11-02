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

	def __init__(self, maze):
		""" Constructor, create our lists. """
		self.wall_list = pygame.sprite.Group()
		self.solution_list = pygame.sprite.Group()
		
		mazeWidth, mazeHeight = maze.getMatrix().shape
		
		self.cell_Width = const.Screen_Width // mazeWidth
		self.cell_Height = const.Screen_Height // mazeHeight
		
		matrix = maze.getMatrix()

		for row in range(mazeHeight):
			for col in range(mazeWidth):
				if matrix[row][col] == const.FULL :
					block = Block( col*self.cell_Width, row*self.cell_Height, self.cell_Width, self.cell_Height, const.BLACK )
					self.wall_list.add(block)

	def addPath(self, path):
		pW = self.cell_Width *.1
		pH = self.cell_Height *.1
		for position in path:
			block = Block( position[1]*self.cell_Width + pW, position[0]*self.cell_Height + pH, self.cell_Width - pW*2, self.cell_Height - pH*2, const.GREEN )
			self.solution_list.add(block)

class App(object):

	def __init__(self, room,  appName = 'Maze Runner'):
		# Call this function so the Pygame library can initialize itself
		pygame.init()
	
		# Create an Width x height sized screen
		self.screen = pygame.display.set_mode([const.Screen_Width, const.Screen_Height])
		# Set the title of the window
		pygame.display.set_caption('Maze Runner')
	
		# Create the player paddle object
		
		self.movingsprites = pygame.sprite.Group()
	
		self.current_room =  room
		
		font = pygame.font.SysFont("comicsansms", 100)

		self.text = font.render("No Way Out", False, const.WHITE)

		self.clock = pygame.time.Clock()

	def display(self, solved):
		""" Main Program """
		
		#self.current_room.addPath( path)
		dsiplay_path = False


		done = False
		while not done:
	
			# --- Event Processing ---
			for event in pygame.event.get():
				if event.type == pygame.QUIT or ( event.type == pygame.KEYUP and event.key  == pygame.K_ESCAPE):
					done = True
				elif event.type == pygame.KEYUP and event.key  == pygame.K_SPACE :
					dsiplay_path = not dsiplay_path
			
			# --- Drawing ---
			self.screen.fill(const.RED)
			self.movingsprites.draw( self.screen)
			self.current_room.wall_list.draw( self.screen)

			if not solved:
				textRect = self.text.get_rect()  
				textRect.center = (const.Screen_Width // 2, const.Screen_Height // 2) 
				self.screen.blit( self.text ,textRect)
				#done = True
			elif dsiplay_path:
				self.current_room.solution_list.draw( self.screen)
			pygame.display.flip()
	
			#self.clock.tick(20)
	
		pygame.quit()
	