def solution():
    total_miles = 650
    current_miles = 200
    day_one_miles = 50
    day_two_miles = 3 * day_one_miles
    total_built = day_one_miles + day_two_miles
    miles_left = total_miles - total_built
    result = miles_left
    
    return result

print(solution())