def solution():
    
    total_episodes = 8
    minutes_per_episode = 44
    monday_minutes = 138
    thursday_minutes = 21
    friday_episodes = 2
    friday_minutes = friday_episodes * minutes_per_episode
    weekend_minutes = (total_episodes * minutes_per_episode) - (monday_minutes + thursday_minutes + friday_minutes)
    result = weekend_minutes
    return result

print(solution())