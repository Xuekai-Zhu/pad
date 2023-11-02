def solution():
    
    planned_calories = 1800
    breakfast_calories = 400
    lunch_calories = 900
    dinner_calories = 1100
    total_calories = breakfast_calories + lunch_calories + dinner_calories
    excess_calories = total_calories - planned_calories
    result = excess_calories
    return result

print(solution())