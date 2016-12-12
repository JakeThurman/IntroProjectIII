import json

def store(file_name, data):
	with open(file_name, 'w') as out_file:
		json.dump(data, out_file)
		
def load(file_name):
	with open('data.txt', 'w') as in_file:
		return json.load(data, in_file)
