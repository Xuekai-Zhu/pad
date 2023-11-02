def solution():
    
    lexie_time_per_mile = 20
    celia_speed_ratio = 2
    celia_time_per_mile = lexie_time_per_mile / celia_speed_ratio
    total_distance = 30
    total_time = total_distance * celia_time_per_mile
    result = total_time
    return result

print(solution())