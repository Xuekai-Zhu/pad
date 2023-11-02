def solution():
    # Define the initial number of brownies
    initial_brownies = 2 * 12

    # Subtract the number of brownies Father ate
    remaining_brownies = initial_brownies - 8

    # Subtract the number of brownies Mooney ate
    remaining_brownies -= 4

    # Add the second batch of brownies
    remaining_brownies += 2 * 12

    result = remaining_brownies
    return result

print(solution())