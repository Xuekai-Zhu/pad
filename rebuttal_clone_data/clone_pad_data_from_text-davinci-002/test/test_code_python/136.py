def solution():
    
    coffee_lbs = 3
    cups_per_lb = 40
    cups_consumed_per_day = 3
    total_cups = coffee_lbs * cups_per_lb
    days_of_coffee = total_cups / cups_consumed_per_day
    result = days_of_coffee
    
    return result

print(solution())