def solution():
    
    total_distance = 23
    distance_after_first_turn = 5
    distance_after_second_turn = 8
    distance_after_fourth_turn = 0   
    distance_after_third_turn = total_distance - distance_after_first_turn - distance_after_second_turn - distance_after_fourth_turn
    result = distance_after_third_turn
    return result

print(solution())