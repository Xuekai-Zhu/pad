def solution():
    
    daily_calories = 2200
    breakfast_calories = 353
    lunch_calories = 885
    snack_calories = 130
    total_calories_consumed = breakfast_calories + lunch_calories + snack_calories
    remaining_calories = daily_calories - total_calories_consumed
    result = remaining_calories
    return result

print(solution())