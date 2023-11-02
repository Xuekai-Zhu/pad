def solution():
    advertised_mpg = 35
    total_miles = 372
    total_gallons = 12
    actual_mpg = total_miles / total_gallons
    diff = advertised_mpg - actual_mpg
    result = diff
    
    return result

print(solution())