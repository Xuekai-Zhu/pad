def solution():
    servings = 4
    cream = 0.5  # in cups
    fat_per_cup = 88

    # Calculate the total amount of fat added
    total_fat = cream * fat_per_cup

    # Calculate the amount of fat added per serving
    fat_per_serving = total_fat / servings
    result = fat_per_serving
    return result

print(solution())