def solution():
    """Ellen’s doctor instructed her to eat a 2,200 calorie a day diet. For breakfast, she ate 353 calories. For lunch, she had 885. She had an afternoon snack of 130 calories. How many calories does she have left for dinner?"""
    # Define Ellen's target calorie intake
    TARGET_CALORIES = 2200

    # Define the number of calories Ellen has eaten
    total_calories = 353 + 885 + 130

    # Calculate the number of calories Ellen has left for dinner
    calories_left = TARGET_CALORIES - total_calories

    # Display the number of calories Ellen has left for dinner
    result = calories_left
    return result

print(solution())