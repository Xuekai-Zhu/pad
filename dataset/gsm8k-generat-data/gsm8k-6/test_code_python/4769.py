def solution():
    # Calculate the total number of episodes in both series
    total_episodes = (12 + 14) * 16

    # Calculate the number of episodes lost due to mechanical failure
    lost_episodes = 2 * (12 + 14)

    # Calculate the number of remaining episodes
    remaining_episodes = total_episodes - lost_episodes
    result = remaining_episodes
    return result

print(solution())