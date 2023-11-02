def solution():
    """Cody goes to the store and buys $40 worth of stuff. The taxes were 5%. After taxes, he got an $8 discount. Cody and his friend split the final price equally. How much did Cody pay?"""
    # Define the initial cost of the purchase
    initial_cost = 40

    # Calculate the tax on the purchase
    tax = initial_cost * 0.05

    # Calculate the cost of the purchase after taxes
    cost_after_tax = initial_cost + tax

    # Subtract the discount from the cost after taxes
    final_cost = cost_after_tax - 8

    # Calculate the amount Cody paid after splitting the final cost with his friend
    cody_paid = final_cost / 2

    result = cody_paid
    return result

print(solution())