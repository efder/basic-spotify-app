from typing import Optional
from spotipy import Spotify, SpotifyClientCredentials
from src.api.helpers.spotifyclient.in_memory_cache_handler import InMemoryCacheHandler
from spotipy import CacheHandler


class SpotifyClientManager:
    _spotify_client: Optional[Spotify] = None

    @classmethod
    def register_spotify_client(cls, cache_handler: Optional[CacheHandler] = None) -> Spotify:
        if not cache_handler:
            cache_handler = InMemoryCacheHandler()
        client_credentials_manager = SpotifyClientCredentials(cache_handler=cache_handler)
        cls._spotify_client = Spotify(client_credentials_manager=client_credentials_manager)
        return cls._spotify_client

    @classmethod
    def get_spotify_client(cls) -> Spotify:
        if not cls._spotify_client:
            raise ValueError('Spotify Client not initialized.')
        return cls._spotify_client
