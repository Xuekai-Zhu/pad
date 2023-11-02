def solution():
    """A dietitian ate three-fourths of her lunch during her lunch break. If the total amount of food she had prepared for lunch had 40 calories, and the recommended calorie intake by the FDA is 25, how many more calories than the recommended amount did she eat?"""
    total_calories = 40
    portion_eaten = 3/4
    calories_eaten = total_calories * portion_eaten
    recommended_calories = 25
    calories_above_recommended = calories_eaten - recommended_calories
    result = calories_above_recommended
    return result

print(solution())