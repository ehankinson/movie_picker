import os
import requests
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")  # make sure your .env has a line like: TMDB_API_KEY=your_key_here

# URL to get popular movies
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

# Send request
response = requests.get(url)
response.raise_for_status()  # optional: will raise error if something goes wrong
data = response.json()

# Print title and poster URL for each movie
for movie in data['results']:
    title = movie['title']
    poster_path = movie['poster_path']
    
    if poster_path:  # Make sure poster exists
        full_poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        full_poster_url = "No poster available"
    
    print(f"{title}: {full_poster_url}")
