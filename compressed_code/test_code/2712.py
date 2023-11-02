def solution():
    
    dishes_per_day = 40
    crab_per_dish = 1.5
    price_per_pound = 8
    days_open_per_week = 7 - 3  
    total_crab_per_week = dishes_per_day * crab_per_dish * days_open_per_week
    total_spent_per_week = total_crab_per_week * price_per_pound
    result = total_spent_per_week
    return result

print(solution())