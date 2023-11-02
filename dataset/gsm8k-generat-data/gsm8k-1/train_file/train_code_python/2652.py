def solution():
    """Mary and her two friends agreed to evenly pay for the cost of 2 pounds of chicken. Mary's mother went to the grocery and bought the 2-pound chicken, 3 pounds of beef that cost $4 per pound, and a liter of oil that costs $1. If Mary's mother paid a total of $16 for the grocery, how much should Mary and her two friends pay each for the chicken?"""
    chicken_cost = 0
    beef_cost = 3 * 4  # 3 pounds of beef at $4 per pound
    oil_cost = 1
    total_cost = 16
    # Solve for chicken_cost
    chicken_cost = (total_cost - beef_cost - oil_cost) / 2
    cost_per_person = chicken_cost / 3
    result = cost_per_person
    return result

print(solution())