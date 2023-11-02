def solution():
    
    coffee_weight = 3
    cups_per_pound = 40
    total_cups = coffee_weight * cups_per_pound
    cups_per_day = 3
    days_of_coffee = total_cups / cups_per_day
    result = days_of_coffee
    return result

print(solution())