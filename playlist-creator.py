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
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
)


def create_playlist(sp, track_ids):
    playlist_name = "My Birthday Hits"
    playlist_description = "As the title states"
    playlist = sp.user_playlist_create(
        SPOTIFY_USER_ID, playlist_name, playlist_description
    )
    playlist_id = playlist["id"]
    sp.user_playlist_add_tracks(username, playlist_id, track_ids)


def find_song(sp, name, artist):
    print(f"Attempting to find {name}")
    results = sp.search(name, limit=5)
    for result in results["tracks"]["items"]:
        if result["artists"][0]["name"] in artist:
            print("Track found on Spotify")
            return result["id"]
    print("Track not found on Spotify")
    return None


def find_tracks(sp, songs):
    tracks_to_be_added = []

    for chart_entry in songs:
        song_id = find_song(sp, chart_entry["title"], chart_entry["artist"])
        if song_id:
            tracks_to_be_added.append(song_id)
    return tracks_to_be_added


def add_tracks_to_playlist(sp, track_ids):
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)


def main():
    token = util.prompt_for_user_token(
        SPOTIFY_USER_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:3000/",
    )
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    # bday = grab_birthday()
    # songs = get_top_songs(bday)
    songs = [
        {"title": "I Will Always Love You", "artist": "Whitney Houston"},
        {"title": "Blem", "artist": "Drake"},
    ]
    track_ids = find_tracks(sp, songs)
    create_playlist(sp, track_ids)
    # track_ids = find_tracks(sp, songs)
    print(track_ids)
    print(f"Found {len(track_ids)} artists out of {len(songs)} tracks")
    # add_tracks_to_playlist(sp)
    print(songs)


if __name__ == "__main__":
    main()
