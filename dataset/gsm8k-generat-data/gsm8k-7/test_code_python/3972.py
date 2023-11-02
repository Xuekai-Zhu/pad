def solution():
    num_strawberries = 12
    strawberry_calories = 4

    yogurt_ounces = 6
    yogurt_calories_per_ounce = 17

    # Calculate the total calories from the strawberries
    strawberry_calories_total = num_strawberries * strawberry_calories

    # Calculate the total calories from the yogurt
    yogurt_calories_total = yogurt_ounces * yogurt_calories_per_ounce

    # Calculate the total calories from both the strawberries and yogurt
    total_calories = strawberry_calories_total + yogurt_calories_total
    result = total_calories
    return result

print(solution())