def solution():
    """Perry made a recipe that serves four people. He added a half cup of cream at the end. Cream has 88 grams of fat per cup. How many grams of fat were added to each serving of food?"""
    servings = 4
    cream_cup = 0.5
    fat_per_cup = 88
    total_fat = cream_cup * fat_per_cup
    fat_per_serving = total_fat / servings
    result = fat_per_serving
    return result

print(solution())