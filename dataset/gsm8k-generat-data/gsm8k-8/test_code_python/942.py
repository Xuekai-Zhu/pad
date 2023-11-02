def solution():
    # Convert movie length to minutes
    movie_length = 1.5 * 60

    # Calculate total time spent running in minutes
    total_time_running = movie_length * 2

    # Convert total time spent running to miles
    miles_run = total_time_running / 12

    result = miles_run
    return result

print(solution())