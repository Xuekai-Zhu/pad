def solution():
    total_seasons = 12
    episodes_per_season = 20
    fraction_watched = 1/3

    # Calculate the total number of episodes in the series
    total_episodes = total_seasons * episodes_per_season

    # Calculate the number of episodes that Cesar has watched
    episodes_watched = fraction_watched * total_episodes

    # Calculate the number of episodes remaining for Cesar to finish the series
    episodes_remaining = total_episodes - episodes_watched

    result = episodes_remaining
    return result

print(solution())