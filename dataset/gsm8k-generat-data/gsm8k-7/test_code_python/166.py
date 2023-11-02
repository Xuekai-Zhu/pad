def solution():
    movie_length = 90
    total_time_tuesday = 4 * 60 + 30  # convert to minutes
    total_time_wednesday = 2 * total_time_tuesday

    # Calculate the maximum number of movies Grandpa could have watched on Tuesday
    max_movies_tuesday = total_time_tuesday // movie_length

    # Calculate the maximum number of movies Grandpa could have watched on Wednesday
    max_movies_wednesday = total_time_wednesday // movie_length

    # Calculate the maximum number of movies Grandpa could have watched during the two days
    max_movies_total = max_movies_tuesday + max_movies_wednesday
    result = max_movies_total
    return result

print(solution())