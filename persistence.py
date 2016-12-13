import json

def store(file_name, data):
	with open(file_name, 'w') as out_file:
		json.dump(data, out_file)
		
def load(file_name):
	with open(file_name, 'r') as in_file:
		return json.load(in_file)
