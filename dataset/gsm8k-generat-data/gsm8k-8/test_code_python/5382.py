def solution():
    # Calculate the total time Emily spent watching TV episodes
    tv_time = 3 * 25

    # Calculate the total time Emily slept
    sleep_time = 4.5 * 60

    # Calculate the total time Emily spent watching movies
    movie_time = 2 * 105

    # Calculate the total time Emily spent on these activities
    total_time = tv_time + sleep_time + movie_time

    # Calculate the remaining time in minutes
    remaining_time = (10 * 60) - total_time

    result = remaining_time
    return result

print(solution())