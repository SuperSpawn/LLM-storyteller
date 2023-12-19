import json

def get_characters():
    with open('data/characters.json') as f:
        return json.load(f)

def get_locations():
    with open('data/locations.json') as f:
        return json.load(f)
