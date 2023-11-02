def solution():
    """A package of candy has 3 servings with 120 calories each. John eats half the package. How many calories did he eat?"""
    # Define the number of servings and calories per serving
    SERVINGS = 3
    CALORIES_PER_SERVING = 120

    # Calculate the total number of calories in the package
    total_calories = SERVINGS * CALORIES_PER_SERVING

    # Calculate the number of calories John ate
    john_calories = total_calories / 2

    # Display the number of calories John ate
    result = john_calories
    return result

print(solution())