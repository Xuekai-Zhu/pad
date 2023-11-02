def solution():
    """Donna can watch 8 episodes each day during weekdays. On each weekend day, she can watch three times the number of episodes she can watch on the weekdays. How many episodes can she watch in a week?"""
    weekday_episodes = 8
    weekend_episodes = 3 * weekday_episodes
    total_weekday_episodes = weekday_episodes * 5
    total_weekend_episodes = weekend_episodes * 2
    total_episodes = total_weekday_episodes + total_weekend_episodes
    result = total_episodes
    return result

print(solution())