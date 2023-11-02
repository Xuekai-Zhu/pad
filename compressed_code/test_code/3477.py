def solution():
    
    cookie_calories = 50
    cracker_calories = 15
    num_cookies = 7
    total_calories_from_cookies = cookie_calories * num_cookies
    remaining_calories_needed = 500 - total_calories_from_cookies
    num_crackers_needed = remaining_calories_needed // cracker_calories
    result = num_crackers_needed
    return result

print(solution())