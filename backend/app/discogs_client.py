import discogs_client
from config import Config

class DiscogsClient:
    def __init__(self):
        self.client = discogs_client.Client('MelodyProduct/1.0', user_token=Config.DISCOGS_TOKEN)

    def search_releases(self, query, limit=5):
        """Search for releases based on a query"""
        results = self.client.search(query, type='release')
        return self._process_release_results(results, limit)

    def _process_release_results(self, results, limit):
        """Process raw release results into a cleaner format"""
        releases = []
        for item in list(results)[:limit]:
            try:
                release = {
                    'title': item.title,
                    'artist': item.artists[0].name if item.artists else 'Unknown',
                    'year': item.year,
                    'label': item.labels[0].name if item.labels else 'Unknown',
                    'format': item.formats[0]['name'] if item.formats else 'Unknown',
                    'discogs_url': f"https://www.discogs.com/release/{item.id}",
                    'thumbnail': item.images[0]['uri'] if item.images else None
                }
                releases.append(release)
            except:
                continue
        return releases

    def get_artist_info(self, artist_name):
        """Get detailed information about an artist"""
        try:
            results = self.client.search(artist_name, type='artist')
            if results:
                artist = results[0]
                return {
                    'name': artist.name,
                    'profile': artist.profile,
                    'urls': artist.urls,
                    'images': [img['uri'] for img in artist.images] if artist.images else []
                }
        except:
            return None 