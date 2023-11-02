def solution():
    """Dalton, Hunter, and Alex started a Superhero Fan Club. They set a goal to watch as many Superhero movies as they could in one summer. Dalton watched 7 movies, Hunter watched 12, and Alex watched 15. They all watched 2 movies together, but every other movie they watched was different. How many different movies did they see?"""
    # Define the number of movies each person watched
    dalton_movies = 7
    hunter_movies = 12
    alex_movies = 15

    # Define the number of movies they watched together
    together_movies = 2

    # Calculate the total number of movies they watched separately
    separate_movies = dalton_movies + hunter_movies + alex_movies - 3 * together_movies

    # Calculate the total number of different movies they saw
    total_movies = together_movies + separate_movies

    # Display the total number of different movies they saw
    result = total_movies
    return result

print(solution())