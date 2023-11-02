def solution():
    """A car is driving through a tunnel with many turns. After a while, the car must travel through a ring that requires a total of 4 right-hand turns. After the 1st turn, it travels 5 meters. After the 2nd turn, it travels 8 meters. After the 3rd turn, it travels a little further and at the 4th turn, it immediately exits the tunnel. If the car has driven a total of 23 meters around the ring, how far did it have to travel after the 3rd turn?"""
    # Define the distances traveled after the 1st and 2nd turns
    distance_1st_turn = 5
    distance_2nd_turn = 8

    # Calculate the total distance traveled after the 1st and 2nd turns
    total_distance_1st_2nd = distance_1st_turn + distance_2nd_turn

    # Calculate the distance traveled after the 3rd turn
    distance_3rd_turn = 23 - total_distance_1st_2nd

    # Return the distance traveled after the 3rd turn
    result = distance_3rd_turn
    return result

print(solution())