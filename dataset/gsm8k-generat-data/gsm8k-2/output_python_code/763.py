def solution():
    """A dietitian ate three-fourths of her lunch during her lunch break. If the total amount of food she had prepared for lunch had 40 calories, and the recommended calorie intake by the FDA is 25, how many more calories than the recommended amount did she eat?"""
    lunch_calories = 40
    recommended_calories = 25
    amount_eaten = 0.75 * lunch_calories
    excess_calories = amount_eaten - recommended_calories
    result = excess_calories
    return result

print(solution())