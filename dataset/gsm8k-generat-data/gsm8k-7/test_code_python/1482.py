def solution():
    episodes_weekday = 8
    episodes_weekend = episodes_weekday * 3
    days_weekday = 5
    days_weekend = 2

    # Calculate the total number of episodes Donna can watch on weekdays
    total_episodes_weekday = episodes_weekday * days_weekday

    # Calculate the total number of episodes Donna can watch on weekends
    total_episodes_weekend = episodes_weekend * days_weekend

    # Calculate the total number of episodes Donna can watch in a week
    total_episodes = total_episodes_weekday + total_episodes_weekend
    result = total_episodes
    return result

print(solution())