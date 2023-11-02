def solution():
    # Calculate the total time for the first movie
    first_movie_time = 1.5

    # Calculate the total time for the second movie
    second_movie_time = first_movie_time + 0.5

    # Calculate the total time for cooking
    cooking_time = (10 * 1) + (20 * 2)

    # Calculate the total time for watching movies and cooking
    total_time = first_movie_time + second_movie_time + cooking_time

    # Convert the total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())