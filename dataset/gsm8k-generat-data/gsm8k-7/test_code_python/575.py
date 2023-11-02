def solution():
    servings_per_package = 3
    calories_per_serving = 120
    total_calories_per_package = servings_per_package * calories_per_serving

    # Calculate the number of calories John ate
    john_servings = servings_per_package / 2
    john_calories = john_servings * calories_per_serving

    result = john_calories
    return result

print(solution())