from .spotify_client import SpotifyClient
from .discogs_client import DiscogsClient
from .email_generator import EmailGenerator
from config import Config

class MusicService:
    def __init__(self):
        self.spotify = SpotifyClient()
        self.discogs = DiscogsClient()
        self.email_generator = EmailGenerator()

    async def process_prompt(self, prompt):
        """Process a user prompt and return relevant music metadata"""
        # Use Claude to interpret the prompt
        interpreted_prompt = await self._interpret_prompt(prompt)
        
        # Search for tracks on Spotify
        spotify_results = self.spotify.search_tracks(interpreted_prompt)
        
        # Enrich with Discogs data
        enriched_results = []
        for track in spotify_results:
            discogs_data = self.discogs.search_releases(
                f"{track['artist']} {track['name']}",
                limit=1
            )
            if discogs_data:
                track.update({
                    'discogs_info': discogs_data[0]
                })
            enriched_results.append(track)
        
        return enriched_results

    async def _interpret_prompt(self, prompt):
        """Use Claude to interpret the user's prompt into searchable terms"""
        response = self.email_generator.client.messages.create(
            model=Config.CLAUDE_MODEL,
            max_tokens=100,
            messages=[{
                "role": "user",
                "content": f"""Interpret this music search prompt into specific search terms:
                {prompt}
                
                Return only the search terms, no explanation needed."""
            }]
        )
        return response.content[0].text.strip()

    def subscribe_to_beta(self, email):
        """Subscribe a user to the beta program via Mailchimp"""
        # This would be implemented when Mailchimp integration is added
        pass 