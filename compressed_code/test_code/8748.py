def solution():
    
    starting_temp = 20
    target_temp = 100
    temp_increase_per_minute = 5
    total_temp_increase = target_temp - starting_temp
    minutes_to_reach_target = total_temp_increase / temp_increase_per_minute
    result = minutes_to_reach_target
    return result

print(solution())