def solution():
    
    cups_per_day = 12
    ounces_per_cup = 8
    ounces_per_bottle = 16
    cups_per_bottle = ounces_per_bottle / ounces_per_cup
    refills_per_day = cups_per_day / cups_per_bottle
    result = refills_per_day
    return result

print(solution())