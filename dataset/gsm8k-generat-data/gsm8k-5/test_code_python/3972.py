def solution():
    strawberries = 12  # Zoe ate 12 strawberries
    yogurt = 6  # Zoe ate 6 ounces of yogurt

    # Calculate the total calories from the strawberries
    strawberry_calories = strawberries * 4  # 4 calories per strawberry

    # Calculate the total calories from the yogurt
    yogurt_calories = yogurt * 17  # 17 calories per ounce

    # Calculate the total calories from the snack
    total_calories = strawberry_calories + yogurt_calories
    result = total_calories
    return result

print(solution())