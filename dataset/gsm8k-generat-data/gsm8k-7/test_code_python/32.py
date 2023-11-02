def solution():
    total_meters = 23
    first_turn_meters = 5
    second_turn_meters = 8
    num_right_turns = 4

    # Calculate the total distance traveled on the first two turns
    first_two_turns_meters = first_turn_meters + second_turn_meters

    # Calculate the remaining distance traveled after the first two turns
    remaining_meters = total_meters - first_two_turns_meters

    # Calculate the distance traveled after the 3rd turn
    third_turn_meters = remaining_meters / (num_right_turns - 2)

    result = third_turn_meters
    return result

print(solution())