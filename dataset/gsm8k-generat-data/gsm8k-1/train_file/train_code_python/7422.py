def solution():
    """A sack of rice, which is 50 kilograms, costs $50. If David sells it for $1.20 per kilogram, how much will be his profit?"""
    cost_price = 50
    selling_price = 1.20
    rice_weight = 50  # in kilograms
    revenue = rice_weight * selling_price
    profit = revenue - cost_price
    result = profit
    return result

print(solution())