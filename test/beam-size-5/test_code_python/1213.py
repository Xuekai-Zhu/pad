def solution():
    
    # Define the initial cost of one visit and the increase percentage
    INITIAL_COST = 2
    INCREASE_PERCENTAGE = 150

    # Calculate the cost of one visit after 5 years
    cost_after_5_years = INITIAL_COST * (1 + INCREASE_PERCENTAGE / 100)

    # Calculate the cost of one visit after 3 years
    cost_after_3_years = cost_after_5_years * 3

    # Display the cost of all visits to the museum
    result = cost_after_3_years
    return result

print(solution())