def solution():
    num_brownies = 24

    # Calculate the total number of brownies consumed by Tina
    num_brownies_consumed = (2 * 5) + (1 * 5) + 4

    # Calculate the number of brownies left
    num_brownies_left = num_brownies - num_brownies_consumed
    result = num_brownies_left
    return result

print(solution())