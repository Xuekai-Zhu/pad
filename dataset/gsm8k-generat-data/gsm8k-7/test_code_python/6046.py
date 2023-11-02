def solution():
    daily_calorie_goal = 2200
    breakfast_calories = 353
    lunch_calories = 885
    snack_calories = 130

    # Calculate the total number of calories Ellen has consumed so far
    total_calories_consumed = breakfast_calories + lunch_calories + snack_calories

    # Calculate the number of calories Ellen has left for dinner
    calories_left = daily_calorie_goal - total_calories_consumed
    result = calories_left
    return result

print(solution())