def solution():
    
    total_distance = 23
    distance_after_turn_1 = 5
    distance_after_turn_2 = 8
    distance_after_turn_3 = total_distance - distance_after_turn_1 - distance_after_turn_2
    result = distance_after_turn_3
    return result

print(solution())