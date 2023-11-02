def solution():
    # Define the variables
    num_builders_1 = 3
    num_builders_2 = 6
    time_1 = 8

    # Calculate the time it would take with 6 builders
    time_2 = (num_builders_1 * time_1) / num_builders_2

    result = time_2
    return result

print(solution())