def solution():
    cake_calories = 110  # Voldemort ate a piece of cake that has 110 calories
    chips_calories = 310  # He also ate 1 pack of chips that contained 310 calories
    coke_calories = 215  # He drank a 500 ml bottle of coke that has 215 calories
    breakfast_calories = 560  # His caloric intake for breakfast is 560 calories
    lunch_calories = 780  # His caloric intake for lunch is 780 calories
    daily_calorie_limit = 2500  # Voldemort has a 2500 calorie intake limit per day

    # Calculate the total calories consumed so far
    total_calories_consumed = cake_calories + chips_calories + coke_calories + breakfast_calories + lunch_calories

    # Calculate the number of calories Voldemort can still consume
    remaining_calories = daily_calorie_limit - total_calories_consumed
    result = remaining_calories
    return result

print(solution())