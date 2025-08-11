from config import Config
import os

class Media():
    _path = None
    _movies = None
    _tv = None
    config = Config()
    total_movies = 0
    total_tv = 0
    movies = []
    def __init__(self):
        if(self.config.get('Media', 'path') is not None):
            self._path = self.config.get('Media', 'path')
            self._movies = self.config.get('Media', 'movies')
            self._tv = self.config.get('Media', 'tv')
            self.get_movies()
            self.get_tv()
    
    def get_movies(self):
        if self._movies is not None:
            print('Getting movies from:', self._movies)
            movies = []
            for item in os.listdir(self._movies):
                if(os.path.isdir(os.path.join(self._movies, item))):
                    movie = {
                        'name': item,
                        'path': os.path.join(self._movies, item),
                        'nfo': os.path.join(self._movies, item, 'movie.nfo') if os.path.exists(os.path.join(self._movies, item, 'movie.nfo')) else None
                    }
                    movies.append(movie)
            self.total_movies = len(movies)
            self.movies = movies
            return movies
    def get_tv(self):
        if self._tv is not None:
            print('Getting tv from:', self._tv)
            tvs = []
            for item in os.listdir(self._tv):
                if(os.path.isdir(os.path.join(self._tv, item))):
                    tv = {
                        'name': item,
                        'path': os.path.join(self._tv, item)
                    }
                    tvs.append(tv)
            self.total_tv = len(tvs)
            return tvs
    def get_movie_by_name(self, movie_name):
        for movie in self.movies:
            if movie['name'] == movie_name:
                return movie
        return None