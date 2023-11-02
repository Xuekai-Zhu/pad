def solution():
    entrance_charge = 4
    price_per_pound = 20
    total_cost = 128
    pounds_picked = (total_cost - entrance_charge) / price_per_pound
    result = pounds_picked
    return result

print(solution())