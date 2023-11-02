def solution():
    """There's an online sale where you get $10 for every $100 that you spend. If you make a purchase of $250 before discounts, how much did you end up paying?"""
    original_price = 250
    discount_amount = (original_price // 100) * 10
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())