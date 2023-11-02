def solution():
    # Calculate the total length of the movies in minutes
    first_movie_length = 90  # 1 hour and 30 minutes
    second_movie_length = first_movie_length + 30  # Second movie is 30 minutes longer
    total_movie_length = first_movie_length + second_movie_length

    # Calculate the total time spent cooking
    popcorn_time = 10
    fries_time = popcorn_time * 2
    total_cooking_time = popcorn_time + fries_time

    # Convert the total time to hours and add to the movie length to get the total time
    total_time = (total_cooking_time + total_movie_length) / 60  # Convert to hours
    result = total_time
    return result

print(solution())