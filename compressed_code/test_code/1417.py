def solution():
    
    north_distance = 100
    east_second_day = 3 * north_distance
    east_third_day = east_second_day + 110
    total_distance = north_distance + east_second_day + east_third_day
    result = total_distance
    return result

print(solution())