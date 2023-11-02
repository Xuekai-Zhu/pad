def solution():
    
    gallons_initial = 3
    ounces_per_gallon = 128
    cups_per_chair = 1
    rows = 5
    chairs_per_row = 10
    total_chairs = rows * chairs_per_row
    total_cups = total_chairs * cups_per_chair
    ounces_per_cup = 6
    total_ounces = total_cups * ounces_per_cup
    ounces_left = (gallons_initial * ounces_per_gallon) - total_ounces
    result = ounces_left
    return result

print(solution())