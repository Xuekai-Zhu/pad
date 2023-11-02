def solution():
    breakfast_calories = 400
    lunch_calories = 900
    dinner_calories = 1100
    total_calories = breakfast_calories + lunch_calories + dinner_calories
    calories_over_plan = total_calories - 1800
    result = calories_over_plan
    return result

print(solution())