def solution():
    time_per_third = 15/60 # converting 15 minutes to hours
    speed_first_third = 16
    speed_second_third = 12
    speed_third_third = 20
    
    distance_first_third = speed_first_third * time_per_third
    distance_second_third = speed_second_third * time_per_third
    distance_third_third = speed_third_third * time_per_third
    
    total_distance = distance_first_third + distance_second_third + distance_third_third
    result = total_distance
    return result

print(solution())