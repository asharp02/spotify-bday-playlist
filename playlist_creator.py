import spotipy
import spotipy.util as util

import credentials
from top_song_finder import grab_birthday, get_top_songs

SPOTIFY_USER_ID = credentials.spotify["SPOTIFY_USER_ID"]
CLIENT_ID = credentials.spotify["CLIENT_ID"]
CLIENT_SECRET = credentials.spotify["CLIENT_SECRET"]
REDIRECT_URI = credentials.spotify["REDIRECT_URI"]

token = util.prompt_for_user_token(
    SPOTIFY_USER_ID,
    scope="playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
)
sp = spotipy.Spotify(auth=token)
sp.trace = False


def create_playlist(track_ids):
    playlist_name = "My Birthday Hits"
    playlist_description = "As the name implies"
    playlist = sp.user_playlist_create(
        SPOTIFY_USER_ID, playlist_name, description=playlist_description
    )
    playlist_id = playlist["id"]
    sp.user_playlist_add_tracks(SPOTIFY_USER_ID, playlist_id, track_ids)


def find_song(name, artist):
    print(f"Attempting to find {name}")
    results = sp.search(name, limit=5)
    for result in results["tracks"]["items"]:
        if result["artists"][0]["name"] in artist:
            print("Track found on Spotify")
            return result["id"]
    print("Track not found on Spotify")
    return None


def find_tracks(songs):
    tracks_to_be_added = []

    for chart_entry in songs:
        song_id = find_song(chart_entry.title, chart_entry.artist)
        if song_id:
            tracks_to_be_added.append(song_id)
    return tracks_to_be_added


def main():
    bday = grab_birthday()
    songs = get_top_songs(bday)
    track_ids = find_tracks(songs)
    create_playlist(track_ids)
    track_ids = find_tracks(songs)


if __name__ == "__main__":
    main()
