def solution():
    """Earl started delivering newspapers on the first floor of a condominium building. He then went up 5 floors then went down 2 floors. He again went up 7 floors and found that he is 9 floors away from the top of the building. How many floors does the building have?"""
    starting_floor = 1
    first_move = 5
    second_move = -2
    third_move = 7
    final_distance = 9
    total_moves = 3  # Earl made three moves in total
    total_distance = (
        starting_floor
        + first_move
        + second_move
        + third_move
        + final_distance
        + (total_moves * 2)
    )  # Add the distance of Earl's moves and the 2 extra floors from each move
    result = total_distance
    return result

print(solution())