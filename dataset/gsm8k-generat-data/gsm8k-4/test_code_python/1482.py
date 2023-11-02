def solution():
    """Donna can watch 8 episodes each day during weekdays. On each weekend day, she can watch three times the number of episodes she can watch on the weekdays. How many episodes can she watch in a week?"""
    # Define the number of episodes Donna can watch on weekdays
    episodes_weekday = 8

    # Calculate the number of episodes Donna can watch on each weekend day
    episodes_weekend = episodes_weekday * 3

    # Calculate the total number of episodes Donna can watch in a week
    total_episodes = (episodes_weekday * 5) + (episodes_weekend * 2)

    # return the result
    result = total_episodes
    return result

print(solution())