def solution():
    # Total number of movies watched
    total_movies = 7 + 12 + 15 - 2  # Subtract 2 because they watched 2 movies together

    # Number of unique movies watched
    unique_movies = total_movies / 3  # There are 3 members of the club

    result = unique_movies
    return result

print(solution())