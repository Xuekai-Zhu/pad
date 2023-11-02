def solution():
    breakfast_calories = 500
    lunch_calories = 1.25 * breakfast_calories
    dinner_calories = 2 * lunch_calories
    shake_calories = 3 * 300

    total_calories = (breakfast_calories + lunch_calories + dinner_calories) * 3 + shake_calories
    result = total_calories
    return result

print(solution())