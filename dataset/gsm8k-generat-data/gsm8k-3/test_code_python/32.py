def solution():
    """A car is driving through a tunnel with many turns. After a while, the car must travel through a ring that requires a total of 4 right-hand turns. After the 1st turn, it travels 5 meters. After the 2nd turn, it travels 8 meters. After the 3rd turn, it travels a little further and at the 4th turn, it immediately exits the tunnel. If the car has driven a total of 23 meters around the ring, how far did it have to travel after the 3rd turn?"""
    # Define the distances traveled after the 1st and 2nd turns
    first_turn_distance = 5
    second_turn_distance = 8

    # Calculate the total distance traveled after the 3rd turn by subtracting the distances from the total distance traveled around the ring
    total_distance = 23
    distance_after_third_turn = total_distance - first_turn_distance - second_turn_distance - second_turn_distance

    # Return the distance traveled after the 3rd turn
    result = distance_after_third_turn
    return result

print(solution())