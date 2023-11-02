def solution():
    """There are 50 passengers on a bus.  At the first stop, 16 more passengers get on the bus. On the other stops, 22 passengers get off the bus and 5 passengers more get on the bus. How many passengers are there on the bus in total at the last station?"""
    # Define the initial number of passengers
    num_passengers = 50

    # Add the passengers from the first stop
    num_passengers += 16

    # Subtract the passengers from the other stops and add the new ones
    num_passengers -= 22
    num_passengers += 5

    # Display the total number of passengers at the last station
    result = num_passengers
    return result

print(solution())