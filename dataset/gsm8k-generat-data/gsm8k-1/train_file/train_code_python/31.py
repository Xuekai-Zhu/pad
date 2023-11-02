def solution():
    """A car is driving through a tunnel with many turns. After a while, the car must travel through a ring that requires a total of 4 right-hand turns. After the 1st turn, it travels 5 meters. After the 2nd turn, it travels 8 meters. After the 3rd turn, it travels a little further and at the 4th turn, it immediately exits the tunnel. If the car has driven a total of 23 meters around the ring, how far did it have to travel after the 3rd turn?"""
    total_distance = 23
    distance_after_first_turn = 5
    distance_after_second_turn = 8
    distance_after_fourth_turn = 0   # Immediately exits the tunnel after this turn
    distance_after_third_turn = total_distance - distance_after_first_turn - distance_after_second_turn - distance_after_fourth_turn
    result = distance_after_third_turn
    return result

print(solution())