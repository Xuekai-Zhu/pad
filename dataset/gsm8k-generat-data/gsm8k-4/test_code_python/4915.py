def solution():
    """Perry made a recipe that serves four people. He added a half cup of cream at the end. Cream has 88 grams of fat per cup. How many grams of fat were added to each serving of food?"""
    # Define the amount of cream added in cups
    cream_cups = 0.5

    # Calculate the total amount of fat added in grams
    total_fat = cream_cups * 88

    # Calculate the amount of fat added to each serving
    fat_per_serving = total_fat / 4

    # Return the result
    result = fat_per_serving
    return result

print(solution())