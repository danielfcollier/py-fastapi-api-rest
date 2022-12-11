import json

def read_json(filepath):
  with open(filepath, "r") as json_file:
    data = json.load(json_file)

  return json.loads(data)

def write_json(filepath, data):
  with open(filepath, "w") as json_file:
    json.dump(data, json_file)
