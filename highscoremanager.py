import persistence 

_FILE_NAME = "data.json"

# Load from the save file.
_high_scores = persistence.load(_FILE_NAME)

def get():
	return _high_scores

def push(score):
	# Add this score, and remove the smallest.
	_high_scores.append(score)
	_high_scores.remove(min(_high_scores))
	
	# Order the scores.
	_high_scores.sort()
	_high_scores.reverse()
	
	# Update save file
	persistence.store(_FILE_NAME, _high_scores)