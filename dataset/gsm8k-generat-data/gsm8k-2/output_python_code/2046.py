def solution():
    """John buys a vacuum cleaner for $250 and a dishwasher for $450. She has a $75 off coupon. How much did he spend?"""
    vacuum_price = 250
    dishwasher_price = 450
    discount = 75
    total_price = vacuum_price + dishwasher_price - discount
    result = total_price
    return result

print(solution())