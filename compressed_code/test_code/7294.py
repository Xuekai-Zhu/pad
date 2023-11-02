def solution():
    
    total_distance = 200
    distance_traveled = total_distance / 4
    time_spent_traveling = 1
    time_spent_lunching = 1
    speed = distance_traveled / time_spent_traveling
    remaining_distance = total_distance - distance_traveled
    remaining_time = remaining_distance / speed
    total_time = time_spent_traveling + time_spent_lunching + remaining_time
    result = total_time
    return result

print(solution())