def solution():
    
    cups_per_day = 8
    cups_per_gallon = 16
    days = 30
    total_cups = cups_per_day * days
    total_gallons = total_cups / cups_per_gallon
    result = total_gallons
    return result

print(solution())