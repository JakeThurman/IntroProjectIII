import pygame, sys, colors, fonts, random, resources, difficulty
from pygame.locals import *
from rendering import *
from screen import Screen
from gridmanager import GridManager

class SymbolSprite(Sprite):
	def __init__(self, pos, symbol):
		super(SymbolSprite, self).__init__(pos[0], pos[1], "symbols/" + symbol.file_name + ".png")
	
class DifficultyScreen(Screen):
	"""Allows the user to select the dificulty of the game
	"""	
	def __init__(self, surface, screen_size, screen_manager):
		"""Constructor for the difficulty selector screen
		"""
		# init parent class
		super(DifficultyScreen, self).__init__()
		
		# Create dependencies
		self._shape_renderer = ShapeRenderer(surface)
		self._sprite_renderer = SpriteRenderer(surface)
		
		font_factory = fonts.random_font_factory()
		self._option_renderer = OptionRenderer(surface, font_factory())
		self._title_renderer = OptionRenderer(surface, font_factory(30))
		
		# Store settings
		self._screen_size = screen_size
		self._screen_manager = screen_manager
		
	def handle_click(self):
		for el, value in self._elements:
			if el.is_hovered:
				self._screen_manager.set(lambda *args: GameScreen(*args, difficulty=value))
	
	def handle_key_up(self, key):
		"""Handles a key up event by begining the game
		"""
		# Close the game if escape is pressed
		if key == K_ESCAPE:
			pygame.quit()
			sys.exit()
			
	def _get_pos(self, i):
		return ((self._screen_size[0] / (len(difficulty.ALL) + 1)) * (i + 1), self._screen_size[1] - self._screen_size[1]/4)
			
	def render(self, refresh_time):
		"""Renderers the screen 
		"""	
		# Set the background
		self._shape_renderer.render_rect((0, 0, self._screen_size[0], self._screen_size[1]), color=colors.DARK_GRAY)

		# Draw the title
		self._title_renderer.render(resources.GAME_NAME, (self._screen_size[0]/2, 50), center=True)
		
		# Reset the rendered element list
		self._elements = []
		
		for i, value in enumerate(difficulty.ALL):
			rend = self._option_renderer.render(value.title, self._get_pos(i), center=True)
			self._elements.append((rend, value))
			
class GameScreen(Screen):
	"""Renderers Game Screen
	"""	
	ROWS = 5
	TITLE_PADDING = 70
	SYMBOLS = ("zinogre", "yang", "white_mana", "weiss", "red_mana", "mh_4", "guitar", "green_mana", "brachy", "blue_mana", "blake", "black_mana")
	
	def __init__(self, surface, screen_size, screen_manager, difficulty):
		"""Constructor for the game screen
		"""
		# init parent class
		super(GameScreen, self).__init__()
		
		# Create dependencies
		self._shape_renderer = ShapeRenderer(surface)
		self._sprite_renderer = SpriteRenderer(surface)
		self._title_renderer = OptionRenderer(surface, fonts.random_font(30))
		
		# Store settings
		self._screen_size = screen_size
		self._screen_manager = screen_manager
				
		self._column_nuber = difficulty.columns
		self._grid_manager = GridManager(GameScreen.ROWS, self._column_nuber, GameScreen.SYMBOLS, colors.ALL)
		
	def handle_click(self):
		pass
	
	def handle_key_up(self, key):
		"""Handles a key up event by begining the game
		"""
		# Close the game if escape is pressed
		if key == K_ESCAPE:
			pygame.quit()
			sys.exit()
	
	def _get_symbol_pos(self, x, y):
		return (x * 100 + 100, y * 100 + 50)
	
	def _get_bg_pos(self, x, y):
		return (x * 100 + 50, y * 100 + 100, x * 100 + 150, y * 100 + 200)

			
	def render(self, refresh_time):
		"""Renderers the screen 
		"""	
		# Set the background
		self._shape_renderer.render_rect((0, 0, self._screen_size[0], self._screen_size[1]), color=colors.DARK_GRAY)
		
		# Draw the title
		self._title_renderer.render(resources.GAME_NAME, (self._screen_size[0]/2, 50), center=True)
		
		# Reset the rendered element list
		self._elements = []
		
		for x, col in enumerate(self._grid_manager.grid):
			for y, symbol in enumerate(col):
				rend = self._shape_renderer.render_rect(self._get_bg_pos(x, y), color=symbol.color)
			
				self._sprite_renderer.render(SymbolSprite(self._get_symbol_pos(x, y), symbol))
				self._elements.append((rend, symbol))
		