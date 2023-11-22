def solution():
    
    # Define the number of sons and the age difference between them
    num_sons = 2
    age_difference = 4

    # Calculate the total age of the two sons
    total_age = 12 + age_difference

    # Calculate the number of candles needed
    candles_needed = total_age * 5

    # Calculate the total cost of the candles
    candles_cost = candles_needed * 3

    # Display the total cost
    result = candles_cost
    return result

print(solution())