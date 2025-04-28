import random

from get_movies import GetMovies

if __name__ == "__main__":
    get_movies = GetMovies()

    amount_of_people = random.randint(2, 10)
    amount_of_movies = random.randint(25, 500)

    movies = get_movies.fetch_movies(amount_of_movies, start_year=2023)
    
    ppls_movies = {}
    for person in range(amount_of_people):
        like_threshold = random.randint(3500, 7000) / 10000
        ppls_movies[person] = set()
        for movie in movies:
            like = random.random()
            if like_threshold > like:
                ppls_movies[person].add(movie["title"])
    
    like_movies = set()
    for i, person in enumerate(ppls_movies):
        if i == 0:
            for movie in ppls_movies[person]:
                like_movies.add(movie)
        else:
            iter_movies = list(like_movies.copy())
            for movie in iter_movies:
                if movie not in ppls_movies[person]:
                    like_movies.remove(movie)
    
    print(f"Amount of people: {amount_of_people}")
    print(f"Amount of movies: {amount_of_movies}")
    print(f"Amount of like movies: {len(like_movies)}")
    for i, movie in enumerate(like_movies):
        print(f"The {i+1}th like movie is {movie}")
    