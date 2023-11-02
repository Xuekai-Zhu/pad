def solution():
    
    # Define the number of goats in Farm X and Farm Y
    goats_X = 55
    goats_Y = 45

    # Define the number of goats sold from Farm X and Farm Y
    goats_X_sold = 10
    goats_Y_sold = goats_X_sold * 2

    # Calculate the total number of goats
    total_goats = goats_X + goats_Y_sold + goats_Y_sold

    # Calculate the number of goats left
    goats_left = total_goats - total_goats

    # Display the number of goats left
    result = goats_left
    return result

print(solution())