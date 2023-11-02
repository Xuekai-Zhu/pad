def solution():
    """Zoe ate a snack of 12 strawberries and 6 ounces of yogurt. If strawberries have 4 calories each and yogurt has 17 calories per ounce, how many calories did Zoe eat?"""
    # Define the number of calories in each strawberry and ounce of yogurt
    STRAWBERRY_CALORIES = 4
    YOGURT_CALORIES = 17

    # Define the number of strawberries and ounces of yogurt that Zoe ate
    strawberries = 12
    yogurt_ounces = 6

    # Calculate the number of calories in the strawberries
    strawberry_calories = strawberries * STRAWBERRY_CALORIES

    # Calculate the number of calories in the yogurt
    yogurt_calories = yogurt_ounces * YOGURT_CALORIES

    # Calculate the total number of calories Zoe ate
    total_calories = strawberry_calories + yogurt_calories

    # Display the total number of calories
    result = total_calories
    return result

print(solution())