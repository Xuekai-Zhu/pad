def solution():
    """John watches a TV show and they announce they are going to do 1 more season. Each season is 22 episodes except for the last season which is 4 episodes longer. There were 9 seasons before the announcement. If each episode is .5 hours how long will it take to watch them all after the last season finishes?"""
    # Define the number of seasons and episodes
    num_seasons = 10
    regular_season_length = 22
    last_season_length = regular_season_length + 4
    episode_length = 0.5

    # Calculate the total number of episodes
    total_episodes = (num_seasons-1) * regular_season_length + last_season_length

    # Calculate the total time to watch all episodes
    total_time = total_episodes * episode_length

    # return the result
    result = total_time
    return result

print(solution())