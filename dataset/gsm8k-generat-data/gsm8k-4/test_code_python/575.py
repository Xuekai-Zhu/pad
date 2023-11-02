def solution():
    """A package of candy has 3 servings with 120 calories each. John eats half the package. How many calories did he eat?"""
    # Calculate the total calories in the package
    total_calories = 3 * 120

    # Calculate the calories John ate (half the package)
    john_calories = total_calories / 2

    # return the result
    result = john_calories
    return result

print(solution())