def solution():
    """Jared wants to watch a series with four episodes. The first three episodes are 58 minutes, 62 minutes, and 65 minutes long respectively. If the four episodes last 4 hours, how long is the fourth episode?"""
    total_minutes = 4 * 60
    first_three_episodes = 58 + 62 + 65
    fourth_episode = total_minutes - first_three_episodes
    result = fourth_episode
    return result

print(solution())