def solution():
    
    monday_to_saturday = 6
    distance_first_leg = 30 * 3
    distance_second_leg = 25 * 4
    total_distance = (distance_first_leg + distance_second_leg) * monday_to_saturday
    result = total_distance
    return result

print(solution())