def solution():
    # Calculate the total amount of fat added to the recipe
    fat_added = (1/2) * 88  # 1/2 cup of cream has 88 grams of fat

    # Calculate the amount of fat added to each serving
    fat_per_serving = fat_added / 4  # the recipe serves 4 people
    result = fat_per_serving
    return result

print(solution())