def solution():
    # Calculate the total time Grandpa Lou spent watching movies on Tuesday
    tuesday_time_in_minutes = 4 * 60 + 30
    tuesday_movies = tuesday_time_in_minutes // 90

    # Calculate the total time Grandpa Lou spent watching movies on Wednesday
    wednesday_movies = 2 * tuesday_movies

    # Calculate the maximum number of full-length movies Grandpa Lou could have watched
    total_movies = tuesday_movies + wednesday_movies
    result = total_movies
    return result

print(solution())