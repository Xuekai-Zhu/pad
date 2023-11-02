def solution():
    """While chatting in the school cafeteria, Cesar's friend Demi tells him that a new fantasy series was on Netflix and he should watch it. The new series has 12 seasons, and each season has 20 episodes. If Cesar watched 1/3 of the series before the school closed, how many episodes were remaining for him to finish the series?"""
    # Define the total number of seasons and episodes
    total_seasons = 12
    episodes_per_season = 20

    # Calculate the total number of episodes in the series
    total_episodes = total_seasons * episodes_per_season

    # Calculate the number of episodes Cesar watched
    episodes_watched = total_episodes / 3

    # Calculate the number of episodes remaining for Cesar to finish the series
    episodes_remaining = total_episodes - episodes_watched

    # Display the number of episodes remaining
    result = episodes_remaining
    return result

print(solution())