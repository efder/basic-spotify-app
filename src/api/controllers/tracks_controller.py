from flask import Response
from flask_restx import Namespace, Resource, abort

from src.api.services.spotify_service import SpotifyService
from src.api.services.genre_service import GenreService

api = Namespace('tracks', description='API for tracks')


@api.route('/<string:genre>')
class GetTopFiveTracksOfArtistInGivenGenre(Resource):
    @api.doc(description='Returns top five tracks of an artist in given genre')
    @api.response(200, 'OK')
    @api.response(404, 'Not Found')
    def get(self, genre: str) -> Response:
        genre = genre.lower()
        random_artist_name = GenreService.get_random_artist_by_genre(genre)
        if not random_artist_name:
            abort(404, 'Requested genre not found.')
        top_five_tracks = SpotifyService.get_top_five_tracks_for_given_artist(random_artist_name)

        return {'data': top_five_tracks}
