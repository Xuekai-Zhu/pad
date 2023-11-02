def solution():
    """Willy is starting a new TV series on Netflix. The TV series has 3 seasons that are each 20 episodes long. If Willy watches 2 episodes a day, how many days will it take for Willy to finish the entire series?"""
    # Define the number of seasons and episodes per season
    num_seasons = 3
    episodes_per_season = 20

    # Calculate the total number of episodes
    total_episodes = num_seasons * episodes_per_season

    # Define the number of episodes watched per day
    episodes_per_day = 2

    # Calculate the number of days it will take to finish the series
    num_days = total_episodes / episodes_per_day

    # Return the result
    result = num_days
    return result

print(solution())