def solution():
    total_turns = 4  # The car must make a total of 4 right-hand turns
    distance_after_1st_turn = 5  # After the 1st turn, the car travels 5 meters
    distance_after_2nd_turn = 8  # After the 2nd turn, the car travels 8 meters
    total_distance = 23  # The car travels a total of 23 meters around the ring

    # Calculate the distance the car traveled after the 3rd turn
    distance_after_3rd_turn = total_distance - distance_after_1st_turn - distance_after_2nd_turn

    result = distance_after_3rd_turn
    return result

print(solution())