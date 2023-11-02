def solution():
    num_seasons_before = 9
    num_episodes_per_season = 22
    extra_episodes_last_season = 4
    episode_length = 0.5  # hours

    # Calculate the total number of episodes before the last season
    total_episodes_before = num_seasons_before * num_episodes_per_season

    # Calculate the total number of episodes including the last season
    total_episodes = total_episodes_before + extra_episodes_last_season

    # Calculate the total amount of time to watch all episodes
    total_time = total_episodes * episode_length
    result = total_time
    return result

print(solution())