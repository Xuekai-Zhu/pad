def solution():
    # Calculate the total number of episodes she can watch during weekdays
    weekday_episodes = 8 * 5

    # Calculate the total number of episodes she can watch during the weekend
    weekend_episodes = 3 * 8 * 2

    # Calculate the total number of episodes she can watch in a week
    total_episodes = weekday_episodes + weekend_episodes
    result = total_episodes
    return result

print(solution())