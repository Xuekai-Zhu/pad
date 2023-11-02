def solution():
    
    weekday_episodes = 8
    weekend_episodes = 3 * weekday_episodes
    total_weekday_episodes = weekday_episodes * 5
    total_weekend_episodes = weekend_episodes * 2
    total_episodes = total_weekday_episodes + total_weekend_episodes
    result = total_episodes
    return result

print(solution())