def solution():
    series1_seasons = 12
    series2_seasons = 14
    episodes_per_season = 16
    lost_episodes = 2

    # Calculate the total number of episodes in each series before the computer failure
    series1_total_episodes = series1_seasons * episodes_per_season
    series2_total_episodes = series2_seasons * episodes_per_season

    # Calculate the total number of lost episodes
    total_lost_episodes = (2 * series1_seasons) + (2 * series2_seasons)

    # Calculate the total number of remaining episodes
    remaining_episodes = (series1_total_episodes + series2_total_episodes) - total_lost_episodes
    result = remaining_episodes
    return result

print(solution())