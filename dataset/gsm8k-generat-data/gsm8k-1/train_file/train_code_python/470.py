def solution():
    """Earl started delivering newspapers on the first floor of a condominium building. He then went up 5 floors then went down 2 floors. He again went up 7 floors and found that he is 9 floors away from the top of the building. How many floors does the building have?"""
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