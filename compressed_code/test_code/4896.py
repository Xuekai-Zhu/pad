def solution():
    
    total_distance = 50
    distance_covered_first_day = 10
    distance_covered_second_day = total_distance / 2
    distance_left = total_distance - distance_covered_first_day - distance_covered_second_day
    result = distance_left
    return result

print(solution())