def solution():
    # Calculate the total number of movies watched
    total_movies = 7 + 12 + 15

    # Subtract 2 movies that they watched together
    total_movies -= 2

    # Calculate the number of different movies watched
    diff_movies = total_movies - (3 * 2)

    result = diff_movies
    return result

print(solution())