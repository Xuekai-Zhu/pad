def solution():
    """There are 50 passengers on a bus. At the first stop, 16 more passengers get on the bus. On the other stops, 22 passengers get off the bus and 5 passengers more get on the bus. How many passengers are there on the bus in total at the last station?"""
    starting_passengers = 50
    first_stop_passengers = starting_passengers + 16
    remaining_stops_passengers = first_stop_passengers - (22 * 4) + (5 * 4)
    result = remaining_stops_passengers
    return result

print(solution())