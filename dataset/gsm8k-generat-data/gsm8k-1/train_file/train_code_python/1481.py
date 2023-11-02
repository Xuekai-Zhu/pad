def solution():
    """Donna can watch 8 episodes each day during weekdays. On each weekend day, she can watch three times the number of episodes she can watch on the weekdays. How many episodes can she watch in a week?"""
    episodes_weekday = 8
    episodes_weekend = episodes_weekday * 3
    days_weekday = 5
    days_weekend = 2
    total_episodes = (episodes_weekday * days_weekday) + (episodes_weekend * days_weekend)
    result = total_episodes
    return result

print(solution())