def solution():
    """Zoe ate a snack of 12 strawberries and 6 ounces of yogurt. If strawberries have 4 calories each and yogurt has 17 calories per ounce, how many calories did Zoe eat?"""
    strawberries = 12
    yogurt_ounces = 6
    strawberry_calories = strawberries * 4
    yogurt_calories = yogurt_ounces * 17
    total_calories = strawberry_calories + yogurt_calories
    result = total_calories
    return result

print(solution())