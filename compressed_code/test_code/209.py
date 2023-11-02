def solution():
    
    total_episodes = 20
    episode_length = 30 
    total_minutes = total_episodes * episode_length
    minutes_per_day = total_minutes / 5
    hours_per_day = minutes_per_day / 60
    result = hours_per_day
    return result

print(solution())