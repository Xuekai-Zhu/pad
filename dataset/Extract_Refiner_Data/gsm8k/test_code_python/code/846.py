def solution():
    
    # Define the initial number of goats
    initial_goats = 55 + 45

    # Define the number of goats sold from Farm X
    goats_sold_x = 10

    # Define the number of goats sold from Farm Y
    goats_sold_y = 2 * goats_sold_x

    # Calculate the number of goats left in the two farms
    goats_left = initial_goats - goats_sold_x - goats_sold_y

    # return the result
    result = goats_left
    return result

print(solution())