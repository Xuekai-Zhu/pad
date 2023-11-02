def solution():
    
    distance_to_market = 30
    time_to_get_home = 0.5
    speed_to_get_home = 20
    distance_to_home = speed_to_get_home * time_to_get_home
    total_distance = distance_to_market + distance_to_home
    result = total_distance
    return result

print(solution())