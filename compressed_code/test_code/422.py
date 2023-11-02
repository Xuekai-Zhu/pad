def solution():
    
    servings_per_package = 3
    calories_per_serving = 120
    total_calories_per_package = servings_per_package * calories_per_serving
    johns_serving_amount = servings_per_package / 2
    johns_total_calorie_amount = johns_serving_amount * calories_per_serving
    result = johns_total_calorie_amount
    return result

print(solution())