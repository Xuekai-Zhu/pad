def solution():
    
    total_distance = 1000
    distance_to_first_sign = 350
    distance_after_second_sign = 275
    distance_between_signs = total_distance - (distance_to_first_sign + distance_after_second_sign)
    result = distance_between_signs
    return result

print(solution())