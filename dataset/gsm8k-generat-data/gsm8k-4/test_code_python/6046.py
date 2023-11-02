def solution():
    """Ellen’s doctor instructed her to eat a 2,200 calorie a day diet. For breakfast, she ate 353 calories. For lunch, she had 885. She had an afternoon snack of 130 calories. How many calories does she have left for dinner?"""
    # Define Ellen's daily calorie limit and the calories she's already consumed
    daily_calories = 2200
    consumed_calories = 353 + 885 + 130

    # Calculate the remaining calories for dinner
    remaining_calories = daily_calories - consumed_calories

    # return the result
    result = remaining_calories
    return result

print(solution())