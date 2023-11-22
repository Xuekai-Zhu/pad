def solution():
    
    # Define the initial cost per minute and the number of minutes
    INITIAL_COST = 0.25
    MAX_MINUTES = 36

    # Calculate the cost of the call before the discount
    first_discount_cost = INITIAL_COST * 16

    # Calculate the cost after the discount
    second_discount_cost = INITIAL_COST * (MAX_MINUTES - 16)

    # Calculate the total cost of the call
    total_cost = first_discount_cost + second_discount_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())