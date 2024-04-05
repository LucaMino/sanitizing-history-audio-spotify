import os
import helper
import create

# loop files
for file in helper.config('files_path'):
    # path file
    file_path = os.path.expanduser('~/' + file)

    # extract data from spotify json
    data = helper.read_spotify_json(file_path)

    # define vars
    artists = []
    sanitize = []
    artists_count = {}
    blacklist = helper.config('blacklist')

    print('Number of songs before sanitization: ' + str(len(data)))

    # loop songs
    for song in data:
        # retrieve artist and track name
        artist = song['master_metadata_album_artist_name']
        track_name = song['master_metadata_track_name']

        # skip podcast ep
        if artist is None or track_name is None: continue

        # remove song
        if artist not in blacklist:
            if all(keyword not in track_name for keyword in blacklist):
                sanitize.append(song)

                # count artists
                artists_count[artist] = artists_count.get(artist, 0) + 1

    print('Number of songs after sanitization: ' + str(len(sanitize)))

    # reorder artist
    sorted_artists = sorted(artists_count.items(), key=lambda x: x[1], reverse=True)

    # show remaining artists
    for artist, count in sorted_artists:
        print(f"x{count} {artist}")

    # create new spotify json
    create.create_spotify_json(sanitize, file_path)