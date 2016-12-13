import persistence 

high_scores = persistence.load("data.json")
def update_high_scores(score):
	global high_scores
	high_scores.append(score)
	high_scores.remove(min(high_scores))
	high_scores.sort()
	high_scores.reverse()
	persistence.store("data.json", high_scores)