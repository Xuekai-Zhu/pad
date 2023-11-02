def solution():
    """James buys 6 t-shirts for 50% off. They each cost $20. How much did he pay?"""
    original_cost = 20
    discount_percent = 50
    num_shirts = 6
    discounted_cost_per_shirt = original_cost * (1 - (discount_percent / 100))
    total_cost = num_shirts * discounted_cost_per_shirt
    result = total_cost
    return result

print(solution())