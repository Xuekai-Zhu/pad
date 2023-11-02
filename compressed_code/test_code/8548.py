def solution():
    
    dishes_per_day = 40
    crab_per_dish = 1.5
    crab_cost_per_pound = 8
    days_per_week = 7 - 3 
    total_crab_used = dishes_per_day * crab_per_dish * days_per_week
    total_cost = total_crab_used * crab_cost_per_pound
    result = total_cost
    return result

print(solution())