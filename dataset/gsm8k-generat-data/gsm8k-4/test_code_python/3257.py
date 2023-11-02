def solution():
    """There are 50 passengers on a bus. At the first stop, 16 more passengers get on the bus. On the other stops, 22 passengers get off the bus and 5 passengers more get on the bus. How many passengers are there on the bus in total at the last station?"""
    # Define the initial number of passengers
    passengers = 50

    # Add the passengers who got on at the first stop
    passengers += 16

    # Subtract the passengers who got off at each subsequent stop
    passengers -= 22
    passengers += 5

    # Display the final number of passengers
    result = passengers
    return result

print(solution())