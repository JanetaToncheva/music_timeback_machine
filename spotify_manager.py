import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from day44 import song_searcher

REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        cache_path='../token.txt',
        show_dialog=True)
)

user = sp.current_user()['id']
year = song_searcher.LOOKBACK_DATE.split('-')[0]
tracks = song_searcher.songs
track_uris = []
song_uri = ''

for track in tracks:
    try:
        song_uri = sp.search(q=f"track:{track}, year={year}", type="track")['tracks']['items'][0]['uri']
    except IndexError:
        pass
    track_uris.append(song_uri)

print(track_uris)

playlist = sp.user_playlist_create(user=user, name=f"{song_searcher.LOOKBACK_DATE} Billboard Top 100",
                        public=False, collaborative=False, description='Top 100 Songs from Billboard')

playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
