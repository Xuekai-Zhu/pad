def solution():
    
    num_people = 4
    cups_per_day = 2
    ounces_per_cup = 0.5
    cost_per_ounce = 1.25
    total_cups_per_week = num_people * cups_per_day * 7
    total_ounces_per_week = total_cups_per_week * ounces_per_cup
    total_cost_per_week = total_ounces_per_week * cost_per_ounce
    result = total_cost_per_week
    return result

print(solution())