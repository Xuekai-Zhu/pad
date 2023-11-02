def solution():
    """Jared wants to watch a series with four episodes. The first three episodes are 58 minutes, 62 minutes, and 65 minutes long respectively. If the four episodes last 4 hours, how long is the fourth episode?"""
    # Define the length of the first three episodes
    episode1 = 58
    episode2 = 62
    episode3 = 65

    # Calculate the total length of the first three episodes in minutes
    total_length = episode1 + episode2 + episode3

    # Calculate the length of the fourth episode in minutes
    fourth_episode = (4*60) - total_length

    # return the result
    result = fourth_episode
    return result

print(solution())