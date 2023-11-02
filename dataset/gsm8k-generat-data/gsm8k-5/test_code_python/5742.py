def solution():
    # Length of the first stick
    stick1 = 3

    # Length of the second stick
    stick2 = 2 * stick1

    # Length of the third stick
    stick3 = stick2 - 1

    # Calculate the total length of all the sticks
    total_length = stick1 + stick2 + stick3
    result = total_length
    return result

print(solution())