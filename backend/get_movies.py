import os
import time
import requests


class GetMovies():

    def __init__(self):
        self.API_KEY = os.getenv("TMDB_API_KEY")
    


    def _check_response(self, response) -> bool:
        codes = [200, 201]
        return response.status_code in codes
      
    


    def fetch_movies(self, amount: int, start_year: int = None, end_year: int = None):
        movies = []
        url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": self.API_KEY,
            "page": None,
            "sort_by": "popularity.desc",
            "include_adult": True,
            "include_video": False
        }
        if start_year:
            params["primary_release_date.gte"] = f"{start_year}-01-01"
        
        if end_year:
            params["primary_release_date.lte"] = f"{end_year}-12-31"
        
        page = 1
        while len(movies) < amount:
            params["page"] = page

            if page != 1 and len(movies) % 800 == 0: # need to wait 5 seconds between each 800 requests
                time.sleep(5)
            
            print(f"Fetching page {page} of {amount} movies")
            response = requests.get(url, params=params) # can only do 40 requests every 10 seconds
            if not self._check_response(response):
                raise Exception(f"Error: {response.status_code} - {response.text}")
            
            data = response.json()
            results = data.get("results", [])
            for movie in results:
                movies.append(movie)
                if len(movies) == amount:
                    break
            
            page += 1
        
        return movies
        


    def get_genres(self):
        genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.API_KEY}&language=en-US"
        genre_response = requests.get(genre_url)
        genres = genre_response.json().get("genres", [])
        return genres

    
    
if __name__ == "__main__":
    get_movies = GetMovies()
    start_year = 2010
    end_year = 2015
    movies = get_movies.fetch_movies(150, start_year, end_year)
    for movie in movies:
        print(movie["title"])
