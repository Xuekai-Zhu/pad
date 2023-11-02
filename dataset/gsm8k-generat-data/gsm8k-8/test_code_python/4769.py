def solution():
    # Calculate the total number of episodes for both series before the computer failure
    total_episodes = (12 + 14) * 16

    # Calculate the number of episodes lost
    episodes_lost = 2 * 4

    # Calculate the total number of episodes after the computer failure
    episodes_remaining = total_episodes - episodes_lost
    result = episodes_remaining
    return result

print(solution())