def solution():
    """A glass of milk is 8 ounces of milk. John drinks 2 glasses of milk. If milk has 3 calories per ounce how many calories did he consume?"""
    glasses_of_milk = 2
    ounces_of_milk = 8 * glasses_of_milk
    calories_per_ounce = 3
    total_calories = ounces_of_milk * calories_per_ounce
    result = total_calories
    return result

print(solution())