def solution():
    """Corey downloaded two movie series from his Netflix account with 12 and 14 seasons per series, respectively. However, in the week, his computer got a mechanical failure, and he lost two episodes from each season for both series. If each season in the movie series that Corey downloaded had 16 episodes, how many episodes remained after the computer's mechanical failure?"""
    # Define the number of seasons and episodes per series
    series_1_seasons = 12
    series_1_episodes = 16
    series_2_seasons = 14
    series_2_episodes = 16

    # Define the number of lost episodes
    lost_episodes = 2 * (series_1_seasons + series_2_seasons)

    # Calculate the number of remaining episodes
    remaining_episodes = (series_1_seasons * series_1_episodes + series_2_seasons * series_2_episodes) - lost_episodes
    
    result = remaining_episodes
    return result

print(solution())