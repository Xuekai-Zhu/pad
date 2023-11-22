def solution():
    
    total_distance = 60
    first_stop_distance = 20
    second_stop_distance = total_distance - first_stop_distance - 15
    distance_traveled = first_stop_distance + second_stop_distance
    result = distance_traveled
    return result

print(solution())