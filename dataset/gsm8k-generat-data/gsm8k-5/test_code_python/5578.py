def solution():
    num_seasons = 3  # The TV series has 3 seasons
    episodes_per_season = 20  # Each season has 20 episodes
    episodes_per_day = 2  # Willy watches 2 episodes per day

    # Calculate the total number of episodes Willy needs to watch
    total_episodes = num_seasons * episodes_per_season

    # Calculate the number of days it will take Willy to finish the series
    num_days = total_episodes / episodes_per_day
    result = num_days
    return result

print(solution())