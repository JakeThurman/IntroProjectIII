import pygame, sys, colors, fonts, random, resources, difficulty
from pygame.locals import *
from rendering import *
from screen import Screen
from gridmanager import GridManager

class SymbolSprite(Sprite):
	def __init__(self, pos, symbol):
		super(SymbolSprite, self).__init__(pos[0], pos[1], "symbols/" + symbol.file_name + ".png", use_alpha=True)
	
class GameOverScreen(Screen):
	"""Shows the user their score.
	"""	
	def __init__(self, surface, screen_size, screen_manager, score, is_win):
		# init parent class
		super(DifficultyScreen, self).__init__()
		
		# Create dependencies
		self._shape_renderer = ShapeRenderer(surface)
		self._sprite_renderer = SpriteRenderer(surface)
		
		font_factory = fonts.random_font_factory()
		self._option_renderer = OptionRenderer(surface, font_factory())
		self._title_renderer = OptionRenderer(surface, font_factory(30), do_hover=False)
		
		# Store settings
		self._screen_size = screen_size
		self._screen_manager = screen_manager
		
		# store score
		self._score = score
	
	def handle_click(self):
		# Go Back twice on click, so the user can choose a new level
		# Once to return to the game, again to the choice screen!
		self._screen_manager.go_back()
		self._screen_manager.go_back()
	
	def render(self, refresh_time):
		# Set the background
		self._shape_renderer.render_rect((0, 0, self._screen_size[0], self._screen_size[1]), color=colors.DARK_GRAY)
		
		# Draw the title
		self._title_renderer.render(resources.GAME_NAME, (self._screen_size[0]/2, 50), center=True, color=colors.WHITE)

		
		
	
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
		self._title_renderer = OptionRenderer(surface, font_factory(30), do_hover=False)
		
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
		self._title_renderer.render(resources.GAME_NAME, (self._screen_size[0]/2, 50), center=True, color=colors.WHITE)
		
		# Reset the rendered element list
		self._elements = []
		
		for i, value in enumerate(difficulty.ALL):
			rend = self._option_renderer.render(value.title, self._get_pos(i), center=True)
			self._elements.append((rend, value))
			
class GameScreen(Screen):
	"""Renderers Game Screen
	"""	
	ROWS = 5
	SQUARE_SIZE = 100
	SYMBOLS = ("zinogre", "yang", "white_mana", "weiss", "red_mana", "mh_4", "guitar", "green_mana", "brachy", "blue_mana", "blake", "black_mana")
	
	def __init__(self, surface, screen_size, screen_manager, difficulty):
		"""Constructor for the game screen
		"""
		# init parent class
		super(GameScreen, self).__init__()
		
		# Create dependencies
		self._shape_renderer = ShapeRenderer(surface)
		self._sprite_renderer = SpriteRenderer(surface)
		
		font_factory = fonts.random_font_factory()
		self._title_renderer = OptionRenderer(surface, font_factory(30), do_hover=False)
		self._score_renderer = OptionRenderer(surface, font_factory(20), do_hover=False)
		
		# Store settings
		self._screen_size = screen_size
		self._screen_manager = screen_manager
				
		self._column_number = difficulty.columns
		self._grid_manager = GridManager(GameScreen.ROWS, self._column_number, GameScreen.SYMBOLS, colors.ALL)
		
		# Initialize State
		self._first_symbol_clicked = None
	
	def handle_click(self):
		for el, symbol in self._elements:
			if el.is_hovered() and self._first_symbol_clicked != symbol:
				if self._first_symbol_clicked != None:
					self._swap(self._first_symbol_clicked, symbol)
					self._first_symbol_clicked = None
				else:
					self._first_symbol_clicked = symbol
					
	def _swap(self, a, b):
		self._grid_manager.swap(a, b)
		
		if self._grid_manager.gridIsSolved():
			self._end_game(is_win=True)
		elif self._grid_manager.score == 0:
			self._end_game(is_win=False)
	
	def _end_game(self, is_win):
		self._screen_manager.set(lambda *args: GameOverScreen(*args, score=self._grid_manager.score, is_win=is_win))
	
	def handle_key_up(self, key):
		"""Handles a key up event by begining the game
		"""
		# Go Back to the difficulty picker screen when escape is pressed
		if key == K_ESCAPE:
			self._screen_manager.go_back()	
		
	def _get_symbol_pos(self, x, y):
		square_pos = self._get_bg_pos(x, y)
		return (square_pos[0], square_pos[1])
	
	def _get_bg_pos(self, x, y):
		ss = GameScreen.SQUARE_SIZE
		
		squares_that_could_fit_on_screen = self._screen_size[0] / ss		
		total_padding_x = (squares_that_could_fit_on_screen - self._column_number) * ss
		left_padding_x = total_padding_x/2
		
		padding_y = self._screen_size[1] - (GameScreen.ROWS * ss)
		
		return (x * ss + left_padding_x, y * ss + padding_y, ss, ss)

	def render(self, refresh_time):
		"""Renderers the screen 
		"""	
		# Set the background
		self._shape_renderer.render_rect((0, 0, self._screen_size[0], self._screen_size[1]), color=colors.DARK_GRAY)
		
		# Draw the title
		self._title_renderer.render(resources.GAME_NAME, (self._screen_size[0]/2, 50), center=True, color=colors.WHITE)
		
		# Output the score
		self._score_renderer.render(resources.SCORE.format(self._grid_manager.score), (self._screen_size[0]/2, 80), center=True, color=colors.SILVER)
		
		# Reset the rendered element list
		self._elements = []
		
		for x, col in enumerate(self._grid_manager.grid):
			for y, symbol in enumerate(col):
				rend = self._shape_renderer.render_rect(self._get_bg_pos(x, y), color=symbol.color)
				self._elements.append((rend, symbol))
			
				self._sprite_renderer.render(SymbolSprite(self._get_symbol_pos(x, y), symbol))
				
				if self._first_symbol_clicked == symbol:
					pass # TODO: DO something to denote this symbol was clicked!
				
		