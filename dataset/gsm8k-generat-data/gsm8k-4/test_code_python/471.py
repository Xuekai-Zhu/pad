def solution():
    """Earl started delivering newspapers on the first floor of a condominium building. He then went up 5 floors then went down 2 floors. He again went up 7 floors and found that he is 9 floors away from the top of the building. How many floors does the building have?"""
    # Define the starting floor and the net change in floors after each move
    starting_floor = 1
    move_1 = 5
    move_2 = -2
    move_3 = 7

    # Calculate Earl's position after each move
    position_after_move_1 = starting_floor + move_1
    position_after_move_2 = position_after_move_1 + move_2
    position_after_move_3 = position_after_move_2 + move_3

    # Calculate the total number of floors in the building
    total_floors = position_after_move_3 + 9

    result = total_floors
    return result

print(solution())