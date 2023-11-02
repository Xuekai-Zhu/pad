def solution():
    """Louise is in a toy store. She already has 28 toys worth $10 each in her cart. On her way to the till she adds 20 teddy bears to the cart. If the $580 in Louise's wallet is exactly enough to pay for all the toys, how much does each teddy bear cost?"""
    # Define the number and cost of the toys already in the cart
    num_toys = 28
    toy_cost = 10

    # Define the number of teddy bears added to the cart
    num_bears = 20

    # Define the total cost of all the toys
    total_cost = 580

    # Calculate the total cost of the new teddy bears
    bear_cost = (total_cost - (num_toys * toy_cost)) / num_bears

    # Display the cost of each teddy bear
    result = bear_cost
    return result

print(solution())