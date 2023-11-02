def solution():
    """Ellen’s doctor instructed her to eat a 2,200 calorie a day diet. For breakfast, she ate 353 calories. For lunch, she had 885. She had an afternoon snack of 130 calories. How many calories does she have left for dinner?"""
    daily_calories = 2200
    calories_consumed = 353 + 885 + 130
    calories_left = daily_calories - calories_consumed
    result = calories_left
    return result

print(solution())