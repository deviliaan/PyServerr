from config import Config
import requests
import os
class TMDB():
    config = None
    api_key = None
    base_url = None
    def __init__(self):
        self.config = Config()
        self.api_key = self.config.get('TMDB', 'api_key')
        self.base_url = "https://api.themoviedb.org/3"
    def search_movie(self, movie_name):
        url = f"{self.base_url}/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        movie = response.json().get('results', [])[0]
        return movie
    def make_movie(self, path,movie):
        if os.path.exists(os.path.join(path, 'movie.nfo')):
            print('NFO file already exists')
            return
        with open(f"{path}/movie.nfo", 'w') as f:
            f.write(f"Title: {movie['title']}\n")
            f.write(f"Overview: {movie['overview']}\n")
            f.write(f"Release Date: {movie['release_date']}\n")
            f.write(f"Rating: {movie['vote_average']}\n")
            f.write(f"Poster Path: https://image.tmdb.org/t/p/w500{movie['poster_path']}\n")
            