def solution():
    # Define the calorie intake for each meal
    breakfast_calories = 400
    lunch_calories = 900
    dinner_calories = 1100

    # Calculate the total calories consumed in a day
    total_calories = breakfast_calories + lunch_calories + dinner_calories

    # Calculate the number of calories over the daily goal
    over_goal = total_calories - 1800
    result = over_goal
    return result

print(solution())