def solution():
    # Define the number of servings and calories per serving
    servings_per_block = 16
    calories_per_serving = 110

    # Calculate the total number of calories in the block
    total_calories = servings_per_block * calories_per_serving

    # Calculate the number of calories Rick has already eaten
    eaten_calories = 5 * calories_per_serving

    # Calculate the number of remaining calories in the block
    remaining_calories = total_calories - eaten_calories
    result = remaining_calories
    return result

print(solution())