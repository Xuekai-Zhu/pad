def solution():
    
    first_day_distance = 1
    current_distance = first_day_distance
    target_distance = 10 * first_day_distance
    
    
    day = 1
    while current_distance < target_distance:
        current_distance *= 2
        day += 1
    
    result = day
    return result

print(solution())