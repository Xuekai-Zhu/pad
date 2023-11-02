def solution():
    """Daphney buys 5 kg of potatoes at the supermarket. If 2 kg of potatoes costs $6, how much will she pay?"""
    # Define the amount of potatoes and the cost of 2 kg of potatoes
    potatoes = 5
    cost_2kg = 6

    # Calculate the cost of 1 kg of potatoes
    cost_1kg = cost_2kg / 2

    # Calculate the total cost of the potatoes
    total_cost = potatoes * cost_1kg

    # return the result
    result = total_cost
    return result

print(solution())