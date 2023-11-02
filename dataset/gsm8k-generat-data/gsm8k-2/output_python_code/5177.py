def solution():
    """Irene shares half of a small apple with her dog every day. A small apple weighs about 1/4 of a pound. She can currently buy apples for $2.00 a pound. How much will she spend so that she and her dog have enough apples to last for 2 weeks?"""
    apples_per_day = 0.5 / 0.25
    days_in_2_weeks = 14
    total_apples_needed = apples_per_day * days_in_2_weeks
    price_per_pound = 2.00
    pounds_needed = total_apples_needed * 0.25
    total_price = pounds_needed * price_per_pound
    result = total_price
    return result

print(solution())