def solution():
    dalton_movies = 7
    hunter_movies = 12
    alex_movies = 15
    together_movies = 2

    # Calculate the total number of movies watched individually
    total_individual_movies = dalton_movies + hunter_movies + alex_movies - together_movies

    result = total_individual_movies
    return result

print(solution())