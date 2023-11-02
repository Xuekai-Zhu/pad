def solution():
    # Calculate the total distance the car travels for the first 3 turns
    total_distance_first_3_turns = 5 + 8 + x

    # Calculate the distance the car travels after the 4th turn
    distance_after_4th_turn = 23 - total_distance_first_3_turns

    # Calculate the distance the car travels after the 3rd turn
    distance_after_3rd_turn = distance_after_4th_turn + x

    # Solve for x using the equation
    x = (23 - 5 - 8) / 2

    result = distance_after_3rd_turn
    return result

print(solution())