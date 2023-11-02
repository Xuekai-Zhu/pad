def solution():
    
    starting_floor = 1
    first_move = 5
    second_move = -2
    third_move = 7
    distance_from_top = 9
    current_floor = starting_floor + first_move + second_move + third_move + distance_from_top
    total_floors = current_floor
    result = total_floors
    return result

print(solution())