def solution():
    """A dietitian ate three-fourths of her lunch during her lunch break. If the total amount of food she had prepared for lunch had 40 calories, and the recommended calorie intake by the FDA is 25, how many more calories than the recommended amount did she eat?"""
    # Define the number of calories in the prepared lunch and the recommended calorie intake
    lunch_calories = 40
    recommended_calories = 25

    # Calculate the number of calories the dietitian ate
    ate_calories = lunch_calories * (3/4)

    # Calculate the number of extra calories the dietitian ate
    extra_calories = ate_calories - recommended_calories

    # Display the number of extra calories
    result = extra_calories
    return result

print(solution())