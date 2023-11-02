def solution():
    burger_calories = 400
    carrot_stick_calories = 20
    cookie_calories = 50
    total_calories_per_kid = 750
    num_carrot_sticks_per_kid = 5

    # Calculate the number of cookies each kid can have
    remaining_calories = total_calories_per_kid - (burger_calories + num_carrot_sticks_per_kid * carrot_stick_calories)
    num_cookies_per_kid = remaining_calories / cookie_calories
    result = num_cookies_per_kid
    return result

print(solution())