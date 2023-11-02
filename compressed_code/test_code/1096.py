def solution():
    
    car_collision_rate = 6  
    big_crash_rate = 3  
    total_time = 4 * 60  
    car_collision_count = car_collision_rate * total_time // 60  
    big_crash_count = big_crash_rate * total_time // 60
    total_accidents = car_collision_count + big_crash_count
    result = total_accidents
    return result

print(solution())