def solution():
    # Calculate the total number of episodes in the series
    total_episodes = 12 * 20

    # Calculate the number of episodes Cesar watched before school closed
    watched_episodes = total_episodes / 3

    # Calculate the number of remaining episodes
    remaining_episodes = total_episodes - watched_episodes
    result = remaining_episodes
    return result

print(solution())