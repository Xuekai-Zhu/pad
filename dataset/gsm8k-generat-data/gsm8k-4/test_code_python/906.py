def solution():
    """The bus started its route. At its first stop, 7 people got on. At the second stop, 3 people got off, and 5 people got on. At the third stop, 2 people got off, and 4 people got on. How many passengers are now on the bus?"""
    # Define the initial number of passengers
    passengers = 0

    # Calculate the number of passengers getting on and off at each stop
    passengers += 7
    passengers -= 3
    passengers += 5
    passengers -= 2
    passengers += 4

    # Return the final number of passengers
    result = passengers
    return result

print(solution())