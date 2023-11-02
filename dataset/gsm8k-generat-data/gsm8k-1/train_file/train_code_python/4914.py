def solution():
    """Perry made a recipe that serves four people. He added a half cup of cream at the end. Cream has 88 grams of fat per cup. How many grams of fat were added to each serving of food?"""
    servings = 4
    cream_added = 0.5 # in cups
    fat_per_cup = 88 # in grams
    fat_per_serving = (cream_added * fat_per_cup) / servings
    result = fat_per_serving
    return result

print(solution())