def solution():
    
    total_distance = 23
    first_turn_distance = 5
    second_turn_distance = 8
    fourth_turn_distance = total_distance - first_turn_distance - second_turn_distance
    third_turn_distance = fourth_turn_distance
    result = third_turn_distance
    return result

print(solution())