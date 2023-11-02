def solution():
    flight_length = 10 * 60  # Convert flight length to minutes
    tv_episode_length = 25
    num_tv_episodes = 3
    sleep_length = 4.5 * 60  # Convert sleep length to minutes
    movie_length = 105  # 1 hour and 45 minutes

    # Calculate the total time spent watching TV episodes
    total_tv_time = tv_episode_length * num_tv_episodes

    # Calculate the total time spent sleeping
    total_sleep_time = sleep_length

    # Calculate the total time spent watching movies
    total_movie_time = movie_length * 2

    # Add up all the time spent on activities
    total_activity_time = total_tv_time + total_sleep_time + total_movie_time

    # Calculate the time remaining in the flight
    time_remaining = flight_length - total_activity_time
    result = time_remaining
    return result

print(solution())