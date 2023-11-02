def solution():
    # Initialize the starting number of passengers on the bus
    num_passengers = 50

    # At the first stop, 16 more passengers get on the bus
    num_passengers += 16

    # At the other stops, 22 passengers get off the bus and 5 more get on
    num_passengers -= 22
    num_passengers += 5

    # Total number of passengers on the bus at the last station
    result = num_passengers
    return result

print(solution())