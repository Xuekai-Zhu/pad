def solution():
    
    # Define the initial cost of the streaming service
    INITIAL_COST = 140

    # Calculate the cost of the streaming service for the first half of the year
    first_half_cost = INITIAL_COST / 2

    # Calculate the cost of the streaming service for the second half of the year
    second_half_cost = INITIAL_COST * 0.9 * 2

    # Calculate the total cost for the streaming service for the end of the year
    total_cost = first_half_cost + second_half_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())