def solution():
    """Daphney buys 5 kg of potatoes at the supermarket. If 2 kg of potatoes costs $6, how much will she pay?"""
    # Define the cost of 2 kg of potatoes
    cost_2kg = 6

    # Calculate the cost of 1 kg of potatoes
    cost_1kg = cost_2kg / 2

    # Calculate the total cost of 5 kg of potatoes
    total_cost = cost_1kg * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())