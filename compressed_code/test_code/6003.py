def solution():
    
    total_episodes = 20
    episode_length = 30  
    num_days = 5
    total_time = total_episodes * episode_length  
    hours_per_day = total_time / (num_days * 60)  
    result = hours_per_day
    return result

print(solution())