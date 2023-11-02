def solution():
    """There are 110 calories in a serving of cheese.  Rick buys the large blocks that have 16 servings per block.  If Rick has already eaten 5 servings of cheese, how many calories are remaining in the block?"""
    # Define the number of servings per block and the calories per serving
    SERVINGS_PER_BLOCK = 16
    CALORIES_PER_SERVING = 110

    # Calculate the total number of calories in a block
    total_calories = SERVINGS_PER_BLOCK * CALORIES_PER_SERVING

    # Calculate the number of servings remaining in the block
    servings_remaining = SERVINGS_PER_BLOCK - 5

    # Calculate the total number of calories remaining in the block
    calories_remaining = servings_remaining * CALORIES_PER_SERVING

    # Display the number of calories remaining in the block
    result = calories_remaining
    return result

print(solution())