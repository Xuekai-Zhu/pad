def solution():
    
    cookies_calories = 50
    crackers_calories = 15
    cookies_consumed = 7
    total_calories = 500
    remaining_calories = total_calories - (cookies_consumed * cookies_calories)
    crackers_needed = remaining_calories / crackers_calories
    result = crackers_needed
    return result

print(solution())