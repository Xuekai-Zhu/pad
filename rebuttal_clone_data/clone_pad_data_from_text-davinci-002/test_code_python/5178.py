def solution():
    apples_needed_per_day = 0.5
    days_needed = 14
    pounds_needed = apples_needed_per_day * days_needed
    price_per_pound = 2
    total_cost = pounds_needed * price_per_pound
    result = total_cost
    return result

print(solution())