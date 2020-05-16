import pygame

BLACK 	= (0, 0, 0)
WHITE 	= (255, 255, 255)
BLUE 	= (0, 0, 255)
GREEN 	= (0, 255, 0)
RED 	= (255, 0, 0)
PURPLE 	= (255, 0, 255)

Screen_Width = 800
Screen_Height = 600

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

import maze 

class Room(object):

	""" Base class for all rooms. """
 
	# Each room has a list of walls, and of enemy sprites.
	block_list = None
	enemy_sprites = None
	cell_Width = None
	cell_Height = None
	def __init__(self, Maze, Path = []):
		""" Constructor, create our lists. """
		self.block_list = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		
		Maze_Width = Maze.width()
		Maze_Height = Maze.height()
		
		self.cell_Width = Screen_Width // Maze_Width
		self.cell_Height = Screen_Height // Maze_Height
		
		matrix = Maze.getMatrix()

		for y in range(Maze_Height):
			for x in range(Maze_Width):
				if matrix[y][x] != 0 :
					block = Block( x*self.cell_Width, y*self.cell_Height, self.cell_Width, self.cell_Height, BLACK )
					self.block_list.add(block)

					
	def addPath(self, Path):
		pW = self.cell_Width *.1
		pH = self.cell_Height *.1
		for loc in Path:
			
			block = Block( loc[1]*self.cell_Width +pW, loc[0]*self.cell_Height +pW, self.cell_Width -pW*2, self.cell_Height -pW*2, GREEN )
			self.block_list.add(block)


import pygame

class App(object):
	def __init__(self, Room, solved ,  appName = 'Maze Runner'):
		# Call this function so the Pygame library can initialize itself
		pygame.init()
	
		# Create an Width x height sized screen
		self.screen = pygame.display.set_mode([Screen_Width, Screen_Height])
		# Set the title of the window
		pygame.display.set_caption('Maze Runner')
	
		# Create the player paddle object
		
		self.movingsprites = pygame.sprite.Group()
	
		self.current_room =  Room
		self.solved =  solved
		
		font = pygame.font.SysFont("comicsansms", 100)

		self.text = font.render("No Way Out", False, WHITE)

		self.clock = pygame.time.Clock()

	def run(self):
		""" Main Program """
		done = False
	
		while not done:
	
			# --- Event Processing ---
	
			for event in pygame.event.get():
				if event.type == pygame.QUIT or ( event.type == pygame.KEYUP and event.key  == pygame.K_ESCAPE):
						done = True
				'''if event.type == pygame.MOUSEBUTTONDOWN:
					current_room.wall_list.add( Wall(event.pos[0], event.pos[1], 20, 20, WHITE) )
				'''
			
			# --- Drawing ---
			self.screen.fill(RED)

			self.movingsprites.draw( self.screen)
			self.current_room.block_list.draw( self.screen)
	
			if not self.solved:
				textRect = self.text.get_rect()  
				textRect.center = (Screen_Width // 2, Screen_Height // 2) 
				self.screen.blit(self.text,textRect)
				#done = True

			pygame.display.flip()
	
			self.clock.tick(20)
	
		pygame.quit()
	