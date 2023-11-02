def solution():
    
    first_day_miles = 200
    second_day_miles = 0.75 * first_day_miles
    combined_miles = first_day_miles + second_day_miles
    third_day_miles = 0.5 * combined_miles
    total_miles = first_day_miles + second_day_miles + third_day_miles
    result = total_miles
    return result

print(solution())