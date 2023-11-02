def solution():
    
    total_distance = 70
    distance_day1 = 20
    distance_day2 = (0.5 * distance_day1) - 6
    distance_day3 = 10
    distance_covered = distance_day1 + distance_day2 + distance_day3
    remaining_distance = total_distance - distance_covered
    result = remaining_distance
    return result

print(solution())