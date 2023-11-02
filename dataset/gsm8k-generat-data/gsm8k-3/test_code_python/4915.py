def solution():
    """Perry made a recipe that serves four people. He added a half cup of cream at the end. Cream has 88 grams of fat per cup. How many grams of fat were added to each serving of food?"""
    # Define the amount of fat in a cup of cream
    CREAM_FAT_PER_CUP = 88
    
    # Define the number of servings in the recipe
    recipe_servings = 4
    
    # Define the amount of cream added
    cream_added = 0.5 # in cups
    
    # Calculate the total amount of fat added
    total_fat_added = CREAM_FAT_PER_CUP * cream_added
    
    # Calculate the amount of fat added per serving
    fat_per_serving = total_fat_added / recipe_servings
    
    # Display the amount of fat added per serving
    result = fat_per_serving
    return result

print(solution())