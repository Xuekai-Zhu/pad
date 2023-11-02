def solution():
    """Donna can watch 8 episodes each day during weekdays. On each weekend day, she can watch three times the number of episodes she can watch on the weekdays. How many episodes can she watch in a week?"""
    # Define the number of episodes Donna can watch on weekdays and weekends
    WEEKDAY_EPISODES = 8
    WEEKEND_EPISODE_MULTIPLIER = 3

    # Calculate the total number of episodes Donna can watch in a week
    weekday_episodes_total = WEEKDAY_EPISODES * 5
    weekend_episodes_total = WEEKDAY_EPISODES * WEEKEND_EPISODE_MULTIPLIER * 2
    total_episodes = weekday_episodes_total + weekend_episodes_total

    # Display the total number of episodes Donna can watch in a week
    result = total_episodes
    return result

print(solution())