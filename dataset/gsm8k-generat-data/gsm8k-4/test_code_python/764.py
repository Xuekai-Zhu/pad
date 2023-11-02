def solution():
    """A dietitian ate three-fourths of her lunch during her lunch break. If the total amount of food she had prepared for lunch had 40 calories, and the recommended calorie intake by the FDA is 25, how many more calories than the recommended amount did she eat?"""
    # Define the total number of calories in the lunch
    lunch_calories = 40

    # Calculate the number of calories the dietitian ate
    ate_calories = lunch_calories * 0.75

    # Calculate the number of calories above the recommended amount
    excess_calories = ate_calories - 25

    # return the result
    result = excess_calories
    return result

print(solution())