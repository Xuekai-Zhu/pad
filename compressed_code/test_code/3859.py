def solution():
    
    tank_size = 12
    advertised_mpg = 35
    total_miles = 372
    actual_mpg = total_miles / tank_size
    difference = advertised_mpg - actual_mpg
    result = difference
    return result

print(solution())