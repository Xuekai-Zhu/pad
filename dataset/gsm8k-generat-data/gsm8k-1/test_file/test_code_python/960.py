def solution():
    """John just started watching a new show. Each episode is 20 minutes long, and there are half as many episodes in total as there are minutes per episode. How many minutes will John spend watching the show if he watches every episode?"""
    episode_length = 20
    total_episodes = episode_length / 2
    total_minutes = episode_length * total_episodes
    result = total_minutes
    return result

print(solution())