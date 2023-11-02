def solution():
    """Corey downloaded two movie series from his Netflix account with 12 and 14 seasons per series, respectively.
    However, in the week, his computer got a mechanical failure, and he lost two episodes from each season for both series.
    If each season in the movie series that Corey downloaded had 16 episodes, how many episodes remained after the computer's mechanical failure?"""
    # Define the number of seasons and episodes per series
    SERIES_1_SEASONS = 12
    SERIES_2_SEASONS = 14
    EPISODES_PER_SEASON = 16

    # Calculate the total number of episodes before the mechanical failure
    total_episodes = (SERIES_1_SEASONS + SERIES_2_SEASONS) * EPISODES_PER_SEASON

    # Calculate the number of episodes lost due to the mechanical failure
    episodes_lost = 2 * (SERIES_1_SEASONS + SERIES_2_SEASONS)

    # Calculate the remaining number of episodes
    remaining_episodes = total_episodes - episodes_lost

    # Display the remaining number of episodes
    result = remaining_episodes
    return result

print(solution())