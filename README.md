# sanitizing-history-audio-spotify
This tool allows users to sanitize Spotify's JSON files by removing specific artists listed in their personal blacklist. This customization ensures the files are cleaned and prepared for importation into various platforms, such as Stats.fm.

## Usage

1. Clone this repository to your local machine.

2. Open the `config/settings.json` file.

3. Configure the paths to your Spotify streaming history audio files under the `file_paths` key.

4. Add the names of artists you wish to remove, including any featuring artists, to the `blacklist` array.

5. Run the tool to sanitize your Spotify streaming history JSON files.

## Example settings.json

```json
{
  "file_paths": [
    "/path/to/spotify_history_1.json",
    "/path/to/spotify_history_2.json"
  ],
  "blacklist": [
    "Artist1",
    "Artist2"
  ]
}