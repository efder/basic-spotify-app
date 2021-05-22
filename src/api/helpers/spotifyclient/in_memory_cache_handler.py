from spotipy.cache_handler import CacheHandler


class InMemoryCacheHandler(CacheHandler):
    def __init__(self, access_token: str = None):
        self.access_token = access_token

    def get_cached_token(self):
        return self.access_token

    def save_token_to_cache(self, access_token: str):
        self.access_token = access_token
