from typing import Dict

from src.api.helpers.spotifyclient.spotify_client_manager import SpotifyClientManager


class SpotifyService:
    @classmethod
    def get_artist_id_by_name(cls, name: str) -> int:
        sp_client = SpotifyClientManager.get_spotify_client()
        artist_id = sp_client.search(name, limit=1, type='artist')['artists']['items'][0]['id']
        return artist_id

    @classmethod
    def get_top_five_tracks_for_given_artist(cls, name: str) -> Dict:
        artist_id = cls.get_artist_id_by_name(name)
        sp_client = SpotifyClientManager.get_spotify_client()
        top_tracks = sp_client.artist_top_tracks(artist_id, 'US')['tracks'][:5]

        result = []
        for track in top_tracks:
            t = {
                'artist': name.title(),
                'track': track['name'],
                'album_image_url': track['album']['images'][0]['url'],
                'release_date': track['album']['release_date']
            }
            result.append(t)

        return result

