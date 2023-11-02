def solution():
    """Mark bought 2 pounds of tomatoes for $5 per pound and 5 pounds of apples, at $6 per pound. How much did he spend in total?"""
    tomato_price_per_pound = 5
    apple_price_per_pound = 6
    tomato_weight = 2
    apple_weight = 5
    total_cost = (tomato_price_per_pound * tomato_weight) + (apple_price_per_pound * apple_weight)
    result = total_cost
    return result

print(solution())