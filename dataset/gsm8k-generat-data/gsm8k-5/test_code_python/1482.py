def solution():
    weekdays = 5  # Number of weekdays 
    weekend_days = 2  # Number of weekend days
    weekday_episodes = 8  # Number of episodes Donna can watch on weekdays
    weekend_episodes = 3 * weekday_episodes  # Number of episodes Donna can watch on weekend days 

    # Calculate the total number of episodes Donna can watch in a week 
    total_episodes = (weekdays * weekday_episodes) + (weekend_days * weekend_episodes)
    result = total_episodes
    return result

print(solution())