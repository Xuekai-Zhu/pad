def solution():
    # Define Earl's starting and ending floors, and the change in floors for each move
    starting_floor = 1
    first_move = 5
    second_move = -2
    third_move = 7
    final_distance = 9

    # Calculate Earl's location after each move
    first_stop = starting_floor + first_move
    second_stop = first_stop + second_move
    third_stop = second_stop + third_move

    # Calculate the total number of floors in the building
    total_floors = third_stop + final_distance
    result = total_floors
    return result

print(solution())