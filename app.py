import pygame
import maze
import const


class App(object):
	def __init__(self, Room,  appName = 'Maze Runner'):
		# Call this function so the Pygame library can initialize itself
		pygame.init()
	
		# Create an Width x height sized screen
		self.screen = pygame.display.set_mode([const.Screen_Width, const.Screen_Height])
		# Set the title of the window
		pygame.display.set_caption('Maze Runner')
	
		# Create the player paddle object
		
		self.movingsprites = pygame.sprite.Group()
	
		self.current_room =  Room
		
		font = pygame.font.SysFont("comicsansms", 100)

		self.text = font.render("No Way Out", False, const.WHITE)

		self.clock = pygame.time.Clock()

	def run(self, solved, path=[]):
		""" Main Program """
		
		self.current_room.addPath( path)
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
			
			if dsiplay_path:
				self.current_room.solution_list.draw( self.screen)
			
			if not solved:
				textRect = self.text.get_rect()  
				textRect.center = (const.Screen_Width // 2, const.Screen_Height // 2) 
				self.screen.blit(self.text,textRect)
				#done = True

			pygame.display.flip()
	
			#self.clock.tick(20)
	
		pygame.quit()
	