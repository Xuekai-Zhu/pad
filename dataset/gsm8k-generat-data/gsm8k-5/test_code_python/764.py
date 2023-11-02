def solution():
    total_calories = 40  # The dietitian had prepared 40 calories worth of food
    fraction_eaten = 3/4  # The dietitian ate three-fourths of her lunch
    calories_eaten = total_calories * fraction_eaten  # Calculate the calories the dietitian ate
    recommended_calories = 25  # The FDA recommends a daily calorie intake of 25

    # Calculate the number of calories the dietitian ate more than the recommended amount
    calories_over_recommendation = calories_eaten - recommended_calories
    result = calories_over_recommendation
    return result

print(solution())