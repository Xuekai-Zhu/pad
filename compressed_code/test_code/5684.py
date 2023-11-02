def solution():
    
    short_show_time = 0.5
    long_show_time = 1
    short_show_episodes = 24
    long_show_episodes = 12
    total_time = short_show_time * short_show_episodes + long_show_time * long_show_episodes
    result = total_time
    return result

print(solution())