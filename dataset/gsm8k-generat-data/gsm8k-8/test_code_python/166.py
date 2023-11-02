def solution():
    # Convert total time watched on Tuesday to minutes
    tuesday_time = 4 * 60 + 30

    # Calculate the number of full-length movies Grandpa watched on Tuesday
    tuesday_movies = tuesday_time // 90

    # Calculate the number of full-length movies Grandpa watched on Wednesday
    wednesday_movies = tuesday_movies * 2

    # Calculate the maximum number of full-length movies Grandpa could have watched
    max_movies = tuesday_movies + wednesday_movies

    result = max_movies
    return result

print(solution())