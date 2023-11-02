def solution():
    
    # Define the initial number of brownies
    initial_brownies = 1 * 12 + 1 * 12

    # Define the number of brownies waiting and eaten
    waiting_brownies = 4 * 12
    eaten_brownies = 1.5 * 12

    # Calculate the total number of brownies
    total_brownies = initial_brownies + waiting_brownies + eaten_brownies

    # Calculate the number of brownies left over
    left_over_brownies = initial_brownies - total_brownies

    # return the result
    result = left_over_brownies
    return result

print(solution())