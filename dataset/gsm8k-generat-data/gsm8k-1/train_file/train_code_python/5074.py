def solution():
    """There's an online sale where you get $10 for every $100 that you spend. If you make a purchase of $250 before discounts, how much did you end up paying?"""
    purchase_price = 250
    discount_rate = 10
    discount_threshold = 100
    dollars_off = (purchase_price // discount_threshold) * discount_rate
    final_price = purchase_price - dollars_off
    result = final_price
    return result

print(solution())