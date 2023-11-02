def solution():
    
    breakfast_calories = 500
    lunch_calories = 1.25 * breakfast_calories
    dinner_calories = 2 * lunch_calories
    total_meal_calories = breakfast_calories + lunch_calories + dinner_calories
    shakes_calories = 3 * 300
    total_calories = total_meal_calories + shakes_calories
    result = total_calories
    return result

print(solution())