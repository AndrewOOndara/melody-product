import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import Config

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=Config.SPOTIFY_CLIENT_ID,
            client_secret=Config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=Config.SPOTIFY_REDIRECT_URI,
            scope=Config.SPOTIFY_SCOPE
        ))

    def search_tracks(self, query, limit=10):
        """Search for tracks based on a query"""
        results = self.sp.search(q=query, limit=limit, type='track')
        return self._process_track_results(results)

    def _process_track_results(self, results):
        """Process raw track results into a cleaner format"""
        tracks = []
        for item in results['tracks']['items']:
            track = {
                'id': item['id'],
                'name': item['name'],
                'artist': item['artists'][0]['name'],
                'album': item['album']['name'],
                'spotify_url': item['external_urls']['spotify'],
                'preview_url': item['preview_url'],
                'album_art': item['album']['images'][0]['url'] if item['album']['images'] else None,
                'release_date': item['album']['release_date'],
                'label': self._get_label_info(item['album']['id'])
            }
            tracks.append(track)
        return tracks

    def _get_label_info(self, album_id):
        """Get label information for an album"""
        try:
            album = self.sp.album(album_id)
            return album.get('label', 'Unknown')
        except:
            return 'Unknown' 