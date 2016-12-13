high_scores = [0, 0, 0]
def update_high_scores(score):
	global high_scores
	high_scores.append(score)
	high_scores.remove(min(high_scores))
	high_scores.sort()
	high_scores.reverse()