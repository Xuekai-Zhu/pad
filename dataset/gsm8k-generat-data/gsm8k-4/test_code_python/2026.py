def solution():
    """Inez has $150. She spends one-half on hockey skates and a certain amount on hockey pads. If Inez has $25 remaining, how much did the hockey pads cost, together, in dollars?"""
    # Define the initial amount of money Inez has
    initial_amount = 150

    # Calculate the amount of money Inez spends on hockey skates
    skates_cost = initial_amount / 2

    # Calculate the amount of money Inez has left for hockey pads
    pads_cost = initial_amount - skates_cost - 25

    result = pads_cost
    return result

print(solution())