def solution():
    
    car_collision_freq = 10
    big_crash_freq = 20

    
    time_in_seconds = 4 * 60

    
    car_collision_count = time_in_seconds // car_collision_freq

    
    big_crash_count = time_in_seconds // big_crash_freq

    
    total_accidents = car_collision_count + big_crash_count

    result = total_accidents
    return result

print(solution())