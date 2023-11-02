def solution():
    # Calculate the total number of hours the theater is open
    total_hours = 8

    # Calculate the length of each movie in hours
    movie_length = 2/60

    # Calculate the total number of movies shown on all screens
    total_movies = 6 * (total_hours / movie_length)

    result = total_movies
    return result

print(solution())