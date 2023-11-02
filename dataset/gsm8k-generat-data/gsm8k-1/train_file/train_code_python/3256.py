def solution():
    """There are 50 passengers on a bus. At the first stop, 16 more passengers get on the bus. On the other stops, 22 passengers get off the bus and 5 passengers more get on the bus. How many passengers are there on the bus in total at the last station?"""
    initial_passengers = 50
    passengers_added_first_stop = 16
    passengers_left_other_stops = 22
    passengers_added_other_stops = 5
    total_passengers = initial_passengers + passengers_added_first_stop - passengers_left_other_stops + passengers_added_other_stops
    result = total_passengers
    return result

print(solution())