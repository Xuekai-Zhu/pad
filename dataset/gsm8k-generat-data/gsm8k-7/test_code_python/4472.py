def solution():
    calories_per_cookie = 50
    calories_per_cracker = 15
    num_cookies = 7
    total_calories_needed = 500

    # Calculate the total calories from the cookies Jimmy ate
    cookie_calories = num_cookies * calories_per_cookie

    # Calculate the remaining calories needed from crackers
    crackers_calories = total_calories_needed - cookie_calories

    # Calculate the number of crackers needed to reach the remaining calories
    num_crackers_needed = crackers_calories / calories_per_cracker
    result = num_crackers_needed
    return result

print(solution())