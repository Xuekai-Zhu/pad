def solution():
    # Calculate the total number of episodes in the series
    total_episodes = 12 * 20

    # Calculate the number of episodes Cesar has watched
    watched_episodes = (1/3) * total_episodes

    # Calculate the number of remaining episodes
    remaining_episodes = total_episodes - watched_episodes
    result = remaining_episodes
    return result

print(solution())