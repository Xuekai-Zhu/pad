def solution():
    
    miles_per_gallon = 400 / 20
    total_miles = 600 * 2
    gallons_needed = (total_miles / miles_per_gallon) - 8
    result = gallons_needed
    return result

print(solution())