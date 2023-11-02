def solution():
    """The bus started its route. At its first stop, 7 people got on. At the second stop, 3 people got off, and 5 people got on. At the third stop, 2 people got off, and 4 people got on. How many passengers are now on the bus?"""
    # Define the initial number of passengers
    passengers = 0

    # Add the 7 people who got on at the first stop
    passengers += 7

    # Subtract the 3 people who got off at the second stop
    passengers -= 3

    # Add the 5 people who got on at the second stop
    passengers += 5

    # Subtract the 2 people who got off at the third stop
    passengers -= 2

    # Add the 4 people who got on at the third stop
    passengers += 4

    # Display the final number of passengers on the bus
    result = passengers
    return result

print(solution())