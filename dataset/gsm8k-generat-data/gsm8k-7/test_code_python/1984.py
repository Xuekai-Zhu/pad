def solution():
    planned_calories = 1800
    breakfast_calories = 400
    lunch_calories = 900
    dinner_calories = 1100

    # Calculate the total number of calories Jacob ate
    total_calories = breakfast_calories + lunch_calories + dinner_calories

    # Calculate the number of calories Jacob went over his plan
    calories_over_plan = total_calories - planned_calories

    result = calories_over_plan
    return result

print(solution())