def solution():
    
    dinner_calories = 110 + 310 + 215
    breakfast_calories = 560
    lunch_calories = 780
    total_calories = dinner_calories + breakfast_calories + lunch_calories
    remaining_calories = 2500 - total_calories
    result = remaining_calories
    return result

print(solution())