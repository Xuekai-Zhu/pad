def solution():
    """If there are sixty-five dolphins in the ocean, and three times that number joins in from a river which has its mouth at the ocean, calculate the total number of dolphins in the ocean."""
    # Define the initial number of dolphins in the ocean
    initial_dolphins = 65

    # Calculate the number of dolphins that join from the river
    river_dolphins = 3 * initial_dolphins

    # Calculate the total number of dolphins in the ocean
    total_dolphins = initial_dolphins + river_dolphins

    # return the result
    result = total_dolphins
    return result

print(solution())