def solution():
    """Cody goes to the store and buys $40 worth of stuff.  The taxes were 5%.  After taxes, he got an $8 discount.  Cody and his friend split the final price equally. How much did Cody pay?"""
    # Define the initial cost and tax rate
    initial_cost = 40
    tax_rate = 0.05

    # Calculate the cost after taxes
    cost_after_tax = initial_cost + (initial_cost * tax_rate)

    # Apply the discount
    cost_after_discount = cost_after_tax - 8

    # Calculate Cody's half of the cost
    cody_cost = cost_after_discount / 2

    # Display Cody's cost
    result = cody_cost
    return result

print(solution())