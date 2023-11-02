def solution():
    """John watches a TV show and they announce they are going to do 1 more season. Each season is 22 episodes except for the last season which is 4 episodes longer. There were 9 seasons before the announcement. If each episode is .5 hours how long will it take to watch them all after the last season finishes?"""
    season_length = 22
    last_season_length = 26
    num_seasons = 10
    total_episodes = (num_seasons - 1) * season_length + last_season_length
    episode_length = 0.5
    total_time = total_episodes * episode_length
    result = total_time
    return result

print(solution())