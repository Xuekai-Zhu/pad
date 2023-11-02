def solution():
    
    coals_per_bag = 60
    total_coals = coals_per_bag * 3
    coals_burned_per_interval = 15
    intervals_needed = total_coals / coals_burned_per_interval
    time_needed = intervals_needed * 20  
    result = time_needed
    return result

print(solution())