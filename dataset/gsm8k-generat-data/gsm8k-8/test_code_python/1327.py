def solution():
    # Define the distance travelled on the first turn
    first_turn_distance = 180

    # Define the distance travelled on the second turn
    second_turn_distance = 0.5 * first_turn_distance + 20

    # Define the total distance travelled
    total_distance = first_turn_distance + second_turn_distance

    # Return the total distance
    return total_distance

print(solution())