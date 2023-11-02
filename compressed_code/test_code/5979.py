def solution():
    
    coffee_weight = 3
    cups_per_lb = 40
    total_cups = coffee_weight * cups_per_lb
    cups_per_day = 3
    days_last = total_cups / cups_per_day
    result = days_last
    return result

print(solution())