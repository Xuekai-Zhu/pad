def solution():
    """Louise is in a toy store. She already has 28 toys worth $10 each in her cart. On her way to the till she adds 20 teddy bears to the cart. If the $580 in Louise’s wallet is exactly enough to pay for all the toys, how much does each teddy bear cost?"""
    # Define the number and cost of the initial toys
    initial_toys = 28
    initial_cost = 10

    # Define the number of teddy bears
    teddy_bears = 20

    # Define the total cost of all the toys
    total_cost = 580

    # Calculate the cost of the teddy bears
    teddy_bear_cost = (total_cost - (initial_toys * initial_cost)) / teddy_bears

    # Return the result
    result = teddy_bear_cost
    return result

print(solution())