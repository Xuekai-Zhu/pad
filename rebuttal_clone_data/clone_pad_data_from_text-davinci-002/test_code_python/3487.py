def solution():
    crab_dishes_per_day = 40
    days_open_per_week = 4
    crab_meat_per_dish = 1.5
    price_per_pound = 8
    pounds_used_per_week = crab_dishes_per_day * days_open_per_week * crab_meat_per_dish
    cost_per_week = pounds_used_per_week * price_per_pound
    result = cost_per_week
    return result

print(solution())