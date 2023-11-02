def solution():
    days_to_premiere = 10
    aired_seasons = 4
    episodes_per_season = 15
    total_episodes = aired_seasons * episodes_per_season
    episodes_per_day = total_episodes / days_to_premiere
    result = episodes_per_day
    return result

print(solution())