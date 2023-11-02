def solution():
    initial_dolphins = 65  # There are initially 65 dolphins in the ocean
    river_dolphins = 3 * initial_dolphins  # Three times the initial number of dolphins join from the river

    # Calculate the total number of dolphins in the ocean
    total_dolphins = initial_dolphins + river_dolphins
    result = total_dolphins
    return result

print(solution())