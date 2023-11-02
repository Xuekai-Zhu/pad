def solution():
    num_episodes = 90
    episode_length = 20  # in minutes
    daily_watch_time = 120  # in minutes per day

    # Calculate the total time required to watch all episodes
    total_watching_time = num_episodes * episode_length

    # Calculate the number of days required to watch all episodes
    num_days = total_watching_time / daily_watch_time

    result = num_days
    return result

print(solution())