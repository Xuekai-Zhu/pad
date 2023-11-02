def solution():
    # Define the initial number of passengers
    passengers = 10

    # Update the number of passengers after the second stop
    passengers -= 3
    passengers += 2 * 10

    # Update the number of passengers after the third stop
    passengers -= 18
    passengers += 2

    result = passengers
    return result

print(solution())