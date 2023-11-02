def solution():
    """A package of candy has 3 servings with 120 calories each. John eats half the package. How many calories did he eat?"""
    servings_per_package = 3
    calories_per_serving = 120
    servings_eaten = servings_per_package / 2
    calories_eaten = servings_eaten * calories_per_serving
    result = calories_eaten
    return result

print(solution())