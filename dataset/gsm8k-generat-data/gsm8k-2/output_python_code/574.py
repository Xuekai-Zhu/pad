def solution():
    """A package of candy has 3 servings with 120 calories each. John eats half the package. How many calories did he eat?"""
    servings_per_package = 3
    calories_per_serving = 120
    total_calories_per_package = servings_per_package * calories_per_serving
    johns_serving_amount = servings_per_package / 2
    johns_total_calorie_amount = johns_serving_amount * calories_per_serving
    result = johns_total_calorie_amount
    return result

print(solution())