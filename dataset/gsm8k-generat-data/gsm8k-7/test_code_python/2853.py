def solution():
    episode_length = 20  # minutes
    filming_factor = 1.5  # 50% longer than episode length
    num_episodes_per_week = 5
    num_weeks = 4

    # Calculate the length of time it takes to film one episode, in minutes
    filming_time_per_episode = episode_length * filming_factor

    # Calculate the total length of time it takes to film one week of episodes, in minutes
    total_filming_time_per_week = filming_time_per_episode * num_episodes_per_week

    # Calculate the total length of time it takes to film all episodes for 4 weeks, in minutes
    total_filming_time = total_filming_time_per_week * num_weeks

    # Convert total filming time from minutes to hours
    total_filming_time_hours = total_filming_time / 60
    result = total_filming_time_hours
    return result

print(solution())