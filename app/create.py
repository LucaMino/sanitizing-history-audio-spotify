import json
import os

def create_spotify_json(data, file_path):
    # retrieve name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    # serializing json
    json_object = json.dumps(data, indent=4)

    # create new file name
    new_file_name = 'results/' + file_name + '_Updated' + file_extension

    # make results dir
    if not os.path.exists('results'):
        os.makedirs('results')

    # writing json
    with open(new_file_name, 'w') as outfile:
        outfile.write(json_object)