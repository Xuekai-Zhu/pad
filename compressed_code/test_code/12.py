def solution():
    
    work_distance = 20 * 2 
    work_days = 5
    weekend_distance = 200
    bike_speed = 25
    total_distance = work_distance * work_days + weekend_distance
    total_time = total_distance / bike_speed
    result = total_time
    return result

print(solution())