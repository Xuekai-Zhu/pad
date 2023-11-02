def solution():
    """A sack of rice, which is 50 kilograms, costs $50. If David sells it for $1.20 per kilogram, how much will be his profit?"""
    rice_weight = 50
    cost_price = 50
    selling_price_per_kg = 1.20
    selling_price = selling_price_per_kg * rice_weight
    profit = selling_price - cost_price
    result = profit
    return result

print(solution())