def solution():
    calories_per_serving = 110  # There are 110 calories in a serving of cheese
    servings_per_block = 16  # There are 16 servings in a large block of cheese
    servings_eaten = 5  # Rick has already eaten 5 servings of cheese

    # Calculate the total number of calories in the block of cheese
    total_calories = calories_per_serving * servings_per_block

    # Calculate the number of remaining servings in the block
    remaining_servings = servings_per_block - servings_eaten

    # Calculate the number of remaining calories in the block
    remaining_calories = remaining_servings * calories_per_serving
    result = remaining_calories
    return result

print(solution())