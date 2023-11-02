def solution():
    calories_per_cookie = 50  # Each cookie contains 50 calories
    calories_per_cracker = 15  # Each cracker contains 15 calories
    cookies_eaten = 7  # Jimmy eats 7 cookies
    total_calories_desired = 500  # Jimmy wants to consume a total of 500 calories

    # Calculate the total number of calories consumed from cookies
    calories_from_cookies = cookies_eaten * calories_per_cookie

    # Calculate the total number of calories needed from crackers
    calories_from_crackers = total_calories_desired - calories_from_cookies

    # Calculate the number of crackers needed to reach the desired number of calories
    crackers_needed = calories_from_crackers / calories_per_cracker
    result = crackers_needed
    return result

print(solution())