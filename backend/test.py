import os
import requests


class GetMovies():

    def __init__(self):
        self.API_KEY = os.getenv("TMDB_API_KEY")
    


    def get_movies(self):
        response = requests.get(self.url)
        response.raise_for_status()
        data = response.json()
        return data
    


    def get_genres(self):
        genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.API_KEY}&language=en-US"
        genre_response = requests.get(genre_url)
        genres = genre_response.json().get("genres", [])
        return genres

    
    
if __name__ == "__main__":
    get_movies = GetMovies()
    genres = get_movies.get_genres()
    genre_dict = {genre['name'].lower(): genre['id'] for genre in genres}
    for g in genre_dict:
        print(g)
