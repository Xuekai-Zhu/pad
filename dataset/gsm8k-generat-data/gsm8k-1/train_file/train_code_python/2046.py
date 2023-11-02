def solution():
    """John buys a vacuum cleaner for $250 and a dishwasher for $450. She has a $75 off coupon. How much did he spend?"""
    vacuum_cleaner_cost = 250
    dishwasher_cost = 450
    coupon_amount = 75
    total_cost = vacuum_cleaner_cost + dishwasher_cost - coupon_amount
    result = total_cost
    return result

print(solution())