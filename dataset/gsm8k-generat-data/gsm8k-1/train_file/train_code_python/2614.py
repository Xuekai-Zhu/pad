def solution():
    """Six bottles of 2 liters of water cost $12. What is the price of 1 liter of water?"""
    total_liters = 12 / 2  # find total liters of water
    price_per_liter = 12 / total_liters  # divide cost by total liters
    result = price_per_liter
    return result

print(solution())