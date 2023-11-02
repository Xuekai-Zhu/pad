def solution():
    
    current_length = 200
    target_length = 650
    first_day_miles = 50
    second_day_miles = 3 * first_day_miles
    total_miles_built = first_day_miles + second_day_miles
    miles_left = target_length - (current_length + total_miles_built)
    result = miles_left
    return result

print(solution())