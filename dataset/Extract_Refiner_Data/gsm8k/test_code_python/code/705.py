def solution():
    
    # Define the number of quarts made in each time period
    CHOCOLATE_QUARTS = 100
    VANILLA_QUARTS = 50

    # Define the time period in hours
    TIME_PERIOD = 2

    # Calculate the total number of quarts made in 48 hours
    total_quarts = (CHOCOLATE_QUARTS + VANILLA_QUARTS) * TIME_PERIOD * 48

    # Display the total number of quarts made
    result = total_quarts
    return result

print(solution())