import requests
from flask import (
    Blueprint, flash, render_template, request
)

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        genre = request.form['genre']
        response = requests.get(f'http://127.0.0.1:5050/tracks/{genre}')
        error = None
        if response.status_code == 404:
            error = "Requested genre not found!"
        if error is None:
            tracks = response.json()["data"]
            return render_template('index/result.html', tracks=tracks)
        flash(error)

    return render_template('index/search.html')
