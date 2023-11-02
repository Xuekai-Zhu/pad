def solution():
    
    time_per_episode = 20
    filming_time_per_episode = time_per_episode * 1.5
    episodes_per_week = 5
    total_filming_time = filming_time_per_episode * episodes_per_week * 4
    total_hours = total_filming_time / 60
    result = total_hours
    return result

print(solution())