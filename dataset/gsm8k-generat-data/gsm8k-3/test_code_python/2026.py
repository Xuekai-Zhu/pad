def solution():
    """Inez has $150. She spends one-half on hockey skates and a certain amount on hockey pads. If Inez has $25 remaining, how much did the hockey pads cost, together, in dollars?"""
    # Define Inez's total initial budget
    initial_budget = 150

    # Calculate the amount spent on hockey skates
    skate_cost = initial_budget / 2

    # Calculate the amount remaining after buying the hockey skates
    remaining_budget = initial_budget - skate_cost

    # Calculate the cost of the hockey pads
    pad_cost = remaining_budget - 25

    # Display the cost of the hockey pads
    result = pad_cost
    return result

print(solution())