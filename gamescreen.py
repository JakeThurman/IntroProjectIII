import pygame, sys, colors, fonts, random
from pygame.locals import *
from rendering import *
from screen import Screen

class GameScreen(Screen):
	"""Renderers Game Screen
	"""

	def __init__(self, surface, screen_size, screen_manager):
		"""Constructor for the game screen
		"""
		# init parent class
		super(GameScreen, self).__init__()
		
		# Create dependencies
		self.shape_renderer = ShapeRenderer(surface)
		self.sprite_renderer = SpriteRenderer(surface)
		self.option_renderer = OptionRenderer(surface, fonts.random_font())
		
		# Store settings
		self._screen_size = screen_size
		self._screen_manager = screen_manager
		
	def handle_click(self):
		pass
	
	def handle_key_up(self, key):
		"""Handles a key up event by begining the game
		"""
		# Close the game if escape is pressed
		if key == K_ESCAPE:
			pygame.quit()
			sys.exit()
			
	def render(self, refresh_time):
		"""Renderers the screen 
		"""	
		print("TODO")