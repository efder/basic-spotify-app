from flask import Blueprint
from flask_restx import Api

from src.api.controllers.tracks_controller import api as tracks_api

bp = Blueprint('main_api', __name__, url_prefix='')
main_api = Api(bp)
main_api.add_namespace(tracks_api)

