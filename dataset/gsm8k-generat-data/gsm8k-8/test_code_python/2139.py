def solution():
    # Define the initial number of dolphins in the ocean
    initial_dolphins = 65

    # Calculate the number of dolphins that join from the river
    river_dolphins = 3 * initial_dolphins

    # Calculate the total number of dolphins in the ocean
    total_dolphins = initial_dolphins + river_dolphins
    result = total_dolphins
    return result

print(solution())