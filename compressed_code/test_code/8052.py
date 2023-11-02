def solution():
    
    episode_length = 20
    filming_time_multiplier = 1.5
    filming_length = episode_length * filming_time_multiplier
    episodes_per_week = 5
    weeks = 4
    total_filming_time = filming_length * episodes_per_week * weeks / 60
    result = total_filming_time
    return result

print(solution())