def solution():
    
    average_speed_1 = 12
    average_speed_2 = 9
    
    hours_driven_1 = 3
    hours_driven_2 = 2
    
    total_hours_driven = hours_driven_1 + hours_driven_2
    total_distance_driven = (average_speed_1 * hours_driven_1) + (average_speed_2 * hours_driven_2)
    
    result = total_distance_driven
    
    return result

print(solution())