def solution():
    # Define the number of servings and calories per serving
    servings = 3
    calories_per_serving = 120

    # Calculate the total number of calories in the package
    total_calories = servings * calories_per_serving

    # Calculate the number of calories John ate (half the package)
    john_calories = 0.5 * total_calories

    result = john_calories
    return result

print(solution())