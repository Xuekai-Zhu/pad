def solution():
    
    current_length = 200
    target_length = 650
    miles_built_day1 = 50
    miles_built_day2 = 3 * miles_built_day1
    total_miles_built = miles_built_day1 + miles_built_day2
    miles_left_to_build = target_length - (current_length + total_miles_built)
    result = miles_left_to_build
    return result

print(solution())