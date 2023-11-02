def solution():
    """John watches a TV show and they announce they are going to do 1 more season. Each season is 22 episodes except for the last season which is 4 episodes longer. There were 9 seasons before the announcement. If each episode is .5 hours how long will it take to watch them all after the last season finishes?"""
    seasons_before_announcement = 9
    standard_season_length = 22
    last_season_length = 26
    episode_length_in_hours = 0.5
    total_episodes = (seasons_before_announcement * standard_season_length) + last_season_length
    total_hours = total_episodes * episode_length_in_hours
    result = total_hours
    return result

print(solution())