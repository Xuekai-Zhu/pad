def solution():
    movie_length = 1.5 # hours
    num_movies = 2
    miles_per_minute = 1/12 # 1 mile in 12 minutes

    # Calculate the total time that Paul spends running
    total_time_running = num_movies * movie_length * 60 # convert hours to minutes

    # Calculate the total distance that Paul runs
    total_distance = total_time_running * miles_per_minute

    result = total_distance
    return result

print(solution())