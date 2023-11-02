def solution():
    num_seasons = 3
    episodes_per_season = 20
    episodes_per_day = 2

    # Calculate the total number of episodes in the entire series
    total_episodes = num_seasons * episodes_per_season

    # Calculate the number of days it will take to finish the entire series
    num_days = total_episodes / episodes_per_day
    result = num_days
    return result

print(solution())