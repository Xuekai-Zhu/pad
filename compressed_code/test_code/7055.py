def solution():
    
    first_day_miles = 200
    second_day_miles = (3/4) * first_day_miles
    total_miles_first_two_days = first_day_miles + second_day_miles
    third_day_miles = 1/2 * total_miles_first_two_days
    total_miles = first_day_miles + second_day_miles + third_day_miles
    result = total_miles
    return result

print(solution())