def solution():
    total_calories = 2200  # Ellen's daily calorie limit is 2200
    calories_consumed = 353 + 885 + 130  # Ellen consumed this many calories in breakfast, lunch, and snack

    # Calculate the remaining calories for dinner
    remaining_calories = total_calories - calories_consumed
    result = remaining_calories
    return result

print(solution())