def solution():
    # Calculate the length of time to film one episode
    episode_film_time = 20 * 1.5

    # Calculate the total time to film 5 episodes
    total_film_time = episode_film_time * 5

    # Convert total film time to hours
    total_film_hours = total_film_time / 60

    # Calculate total film time for 4 weeks
    total_film_time_4_weeks = total_film_hours * 4

    result = total_film_time_4_weeks
    return result

print(solution())