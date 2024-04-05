import os
import json

# load config/.json file
def load_json(name = 'settings.json'):
    # absolute path
    current_dir = os.path.dirname(__file__)
    # build settings.json path
    settings_path = os.path.join(current_dir, 'config', name)
    # load file
    with open(settings_path, 'r') as f:
        settings = json.load(f)
    # return file content
    return settings

# retrieve config param from key (settings.json)
def config(key):
    # return array of splitted keys
    elements = key.split('.') if '.' in key else [key]
    # load config file
    settings = load_json()

    for element in elements:
        # create settings[element1][element2]...
        settings = settings.setdefault(element, {})

    return settings

# read spotify json
def read_spotify_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)