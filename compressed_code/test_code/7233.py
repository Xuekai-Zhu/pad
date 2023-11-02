def solution():
    
    north_distance = 100
    east_distance_second_day = north_distance * 3
    east_distance_third_day = east_distance_second_day + 110
    total_distance = north_distance + east_distance_second_day + east_distance_third_day
    result = total_distance
    return result

print(solution())