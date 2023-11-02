def solution():
    """Willy is starting a new TV series on Netflix. The TV series has 3 seasons that are each 20 episodes long. If Willy watches 2 episodes a day, how many days will it take for Willy to finish the entire series?"""
    # Define the number of seasons and episodes per season
    seasons = 3
    episodes_per_season = 20

    # Calculate the total number of episodes in the series
    total_episodes = seasons * episodes_per_season

    # Calculate the number of days it will take to watch the entire series
    days_to_finish = total_episodes / 2

    # Display the number of days
    result = days_to_finish
    return result

print(solution())