def solution():
    num_full_seasons = 4
    episodes_per_season = 15
    days_until_premiere = 10

    # Calculate the total number of episodes Joe needs to watch
    total_episodes = num_full_seasons * episodes_per_season

    # Calculate the number of episodes Joe needs to watch per day to catch up
    episodes_per_day = total_episodes / days_until_premiere
    result = episodes_per_day
    return result

print(solution())