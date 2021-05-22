from typing import Dict, List, Optional
import random


class GenreService:
    _genre_artist_mapping: Optional[Dict[str, List[str]]]

    @classmethod
    def register_genre_service(cls, genre_artist_mapping: Optional[Dict[str, List[str]]]) -> None:
        cls._genre_artist_mapping = genre_artist_mapping

    @classmethod
    def get_genre_artist_mapping(cls) -> Optional[Dict[str, List[str]]]:
        if not cls._genre_artist_mapping:
            raise ValueError('Genre artist mapping not initialized.')
        return cls._genre_artist_mapping

    @classmethod
    def _get_artists_by_genre(cls, genre: str) -> Optional[List[str]]:
        if cls._genre_artist_mapping and genre in cls._genre_artist_mapping:
            return cls._genre_artist_mapping[genre]
        return None

    @classmethod
    def get_random_artist_by_genre(cls, genre: str) -> Optional[List[str]]:
        artists = cls._get_artists_by_genre(genre)
        if not artists:
            return None
        return random.choice(artists)


