def solution():
    # Calculate the calories from the burger and carrot sticks
    burger_calories = 400
    carrot_sticks_calories = 5 * 20  # each carrot stick has 20 calories
    total_calories_without_cookies = burger_calories + carrot_sticks_calories

    # Calculate the number of cookies needed to reach a total of 750 calories
    total_calories_with_cookies = 750
    cookies_calories = total_calories_with_cookies - total_calories_without_cookies
    cookies_per_kid = cookies_calories // 50  # each cookie has 50 calories

    result = cookies_per_kid
    return result

print(solution())