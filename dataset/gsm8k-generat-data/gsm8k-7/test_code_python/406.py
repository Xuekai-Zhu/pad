def solution():
    first_movie_length = 90  # in minutes
    second_movie_length = first_movie_length + 30  # in minutes

    popcorn_prep_time = 10  # in minutes
    fries_prep_time = 2 * popcorn_prep_time  # in minutes

    # Calculate the total time spent cooking
    total_cooking_time = popcorn_prep_time + fries_prep_time

    # Calculate the total time spent watching the movies
    total_movie_time = (first_movie_length + second_movie_length) / 60  # convert to hours

    # Calculate the total time spent cooking and watching the movies
    total_time = total_cooking_time / 60  # convert to hours
    total_time += total_movie_time

    result = total_time
    return result

print(solution())