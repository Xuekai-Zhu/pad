def solution():
    """Ellen’s doctor instructed her to eat a 2,200 calorie a day diet. For breakfast, she ate 353 calories. For lunch, she had 885. She had an afternoon snack of 130 calories. How many calories does she have left for dinner?"""
    daily_calories = 2200
    breakfast_calories = 353
    lunch_calories = 885
    snack_calories = 130
    total_calories_consumed = breakfast_calories + lunch_calories + snack_calories
    remaining_calories = daily_calories - total_calories_consumed
    result = remaining_calories
    return result

print(solution())