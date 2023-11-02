def solution():
    """Corey downloaded two movie series from his Netflix account with 12 and 14 seasons per series, respectively. However, in the week, his computer got a mechanical failure, and he lost two episodes from each season for both series. If each season in the movie series that Corey downloaded had 16 episodes, how many episodes remained after the computer's mechanical failure?"""
    total_seasons = 12 + 14
    lost_episodes = 2 * 16 * total_seasons
    remaining_episodes = 16 * total_seasons - lost_episodes
    result = remaining_episodes
    return result

print(solution())