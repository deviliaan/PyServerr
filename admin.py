from flask import Blueprint, render_template, request,redirect
from media import Media
from config import Config
from tmdb import TMDB
admin = Blueprint('admin', __name__)
config = Config()
tmdb = TMDB()


@admin.route('/dashboard', methods=['GET'])
def dashboard():
    # This route would typically require authentication
    media = Media()
    return render_template('admin/dashboard.html',movies_count=media.total_movies,tv_count=media.total_tv)

@admin.route('/movies', methods=['GET'])
def movies():
    media = Media()
    movies = media.get_movies()
    return render_template('admin/movies.html', movies=movies)


@admin.route('/movies/nfo/<string:movie_name>', methods=['GET'])
def movie_nfo(movie_name):
    media = Media()
    movie = media.get_movie_by_name(movie_name)
    if(movie['nfo'] is None):
        res = tmdb.search_movie(movie_name)
        tmdb.make_movie(movie['path'], res)
        return redirect('/admin/movies')
    else:
        return redirect('/admin/movies')