def solution():
    daily_calories = 2200
    breakfast_calories = 353
    lunch_calories = 885
    snack_calories = 130
    dinner_calories = daily_calories - breakfast_calories - lunch_calories - snack_calories
    result = dinner_calories
    return result

print(solution())