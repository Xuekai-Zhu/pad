def solution():
    
    # Define the initial number of passengers
    passengers = 48

    # On the first stop, 8 passengers get off
    passengers -= 8

    # On the second stop, 21 passengers get off
    passengers -= (5 * 8)

    # On the second stop, 3 times fewer passengers get on
    passengers -= (3 * 21)

    # Display the final number of passengers
    result = passengers
    return result

print(solution())