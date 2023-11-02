def solution():
    
    parking_time = 5
    walking_time = 3
    crowded_days = 2
    crowded_time = 30
    non_crowded_days = 3
    non_crowded_time = 10
    work_days = 5
    
    total_parking_time = parking_time * work_days
    total_walking_time = walking_time * work_days
    total_crowded_time = crowded_days * crowded_time
    total_non_crowded_time = non_crowded_days * non_crowded_time
    
    total_time = total_parking_time + total_walking_time + total_crowded_time + total_non_crowded_time
    result = total_time
    
    return result

print(solution())