def solution():
    
    # Define the number of servings in a bag and the calories per serving
    SERVINGS_PER_BAG = 5
    CALORIES_PER_SERVING = 250

    # Define the target daily calorie target
    TARGET_DAILY_CALORIES = 2000

    # Calculate the total number of servings in the bag
    total_servings = SERVINGS_PER_BAG * TARGET_DAILY_CALORIES / CALORIES_PER_SERVING

    # Calculate the total calories consumed
    total_calories_consumed = 1800

    # Calculate the remaining calories that can be eaten
    remaining_calories = total_servings * CALORIES_PER_SERVING

    # Calculate the total grams that can be eaten
    total_grams = remaining_calories / 1000

    # Display the total grams that can be eaten
    result = total_grams
    return result

print(solution())