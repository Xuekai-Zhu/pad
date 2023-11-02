def solution():
    first_movie_time = 2
    second_movie_time = first_movie_time * 1.5
    third_movie_time = (first_movie_time + second_movie_time) - 1

    # Calculate the total time of the movie marathon
    total_time = first_movie_time + second_movie_time + third_movie_time
    result = total_time
    return result

print(solution())