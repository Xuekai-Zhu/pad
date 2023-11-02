def solution():
    """Daphney buys 5 kg of potatoes at the supermarket. If 2 kg of potatoes costs $6, how much will she pay?"""
    potatoes_per_cost = 2
    cost_per_potatoes = 6 / potatoes_per_cost
    total_cost = cost_per_potatoes * 5
    result = total_cost
    return result

print(solution())