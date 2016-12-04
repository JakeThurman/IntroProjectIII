import resources

class Difficulty:	
	def __init__(self, title, columns):
		self.title = title
		self.columns = columns
	
EASY = Difficulty(resources.DIFFICULTY_EASY, 3)
MEDUIM = Difficulty(resources.DIFFICULTY_MEDIUM, 5)
HARD = Difficulty(resources.DIFFICULTY_HARD, 7)

ALL = (EASY, MEDUIM, HARD)