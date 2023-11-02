def solution():
    """Jan buys 5 dozen roses.  Each rose cost $6.  Since he bought so many he only needs to pay 80%.  How much did he pay?"""
    # Define the cost per rose
    COST_PER_ROSE = 6

    # Define the number of dozens purchased
    dozens_purchased = 5

    # Calculate the total cost before discount
    total_cost = dozens_purchased * 12 * COST_PER_ROSE

    # Apply the 80% discount
    discounted_cost = total_cost * 0.8

    # Display the final cost after discount
    result = discounted_cost
    return result

print(solution())