from flask import Flask
import json


def create_app() -> Flask:
    app = Flask(__name__)

    from src.api.helpers.spotifyclient.spotify_client_manager import SpotifyClientManager
    SpotifyClientManager.register_spotify_client()

    with open('genres.json', 'r') as f:
        genres = json.load(f)

    from src.api.services.genre_service import GenreService
    GenreService.register_genre_service(genres)

    from src.api.controllers import bp as main_api
    app.register_blueprint(main_api, url_prefix='')

    return app
