def solution():
    """There are 200 snakes in a park. There are three times as many pythons as boa constrictors. If there 40 boa constrictors and the rest of the snakes are rattlesnakes, calculate the total number of rattlesnakes in the park."""
    # Define the total number of snakes
    total_snakes = 200
    
    # Calculate the number of pythons (three times the number of boa constrictors)
    pythons = 3 * 40
    
    # Calculate the number of boa constrictors
    boa_constrictors = 40
    
    # Calculate the number of rattlesnakes (the remaining number of snakes)
    rattlesnakes = total_snakes - pythons - boa_constrictors
    
    # Return the result
    result = rattlesnakes
    return result

print(solution())