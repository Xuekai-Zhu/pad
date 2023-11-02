def solution():
    servings_per_package = 3  # The package of candy has 3 servings
    calories_per_serving = 120  # Each serving has 120 calories
    total_calories = servings_per_package * calories_per_serving  # The total number of calories in the package

    # Calculate the number of calories John ate (half the package)
    calories_eaten = (1/2) * total_calories
    result = calories_eaten
    return result

print(solution())