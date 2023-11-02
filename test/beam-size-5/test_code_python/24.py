def solution():
    
    total_distance = 60
    first_stop_distance = 20
    second_stop_distance = 15
    first_stop_distance = first_stop_distance + second_stop_distance
    distance_between_stops = total_distance - first_stop_distance
    result = distance_between_stops
    return result

print(solution())