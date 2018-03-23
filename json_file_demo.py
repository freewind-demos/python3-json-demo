import json
import os

data_file = './data.json'
if not os.path.exists(data_file):
    open(data_file, 'a').close()

with open(data_file, 'w') as f:
    json.dump({"name": "Freewind", "age": 1000}, f)

with open(data_file, 'r') as f:
    print(json.load(f))
