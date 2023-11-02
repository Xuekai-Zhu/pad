def solution():
    servings = 4  # The recipe serves 4 people
    cream_per_serving = 0.5 / servings  # Perry added half cup of cream, so each serving gets 1/4 cup
    fat_per_cup = 88  # Cream has 88 grams of fat per cup

    # Calculate the grams of fat added to each serving of food
    fat_per_serving = cream_per_serving * fat_per_cup
    result = fat_per_serving
    return result

print(solution())