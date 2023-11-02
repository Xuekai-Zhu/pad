def solution():
    # Calculate the total number of episodes Donna can watch in a week
    weekdays = 5
    weekend_days = 2
    weekday_episodes = 8
    weekend_episodes = 3 * weekday_episodes
    total_episodes = weekdays * weekday_episodes + weekend_days * weekend_episodes
    result = total_episodes
    return result

print(solution())