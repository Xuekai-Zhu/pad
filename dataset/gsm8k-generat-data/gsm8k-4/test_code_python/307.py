def solution():
    """There are 110 calories in a serving of cheese. Rick buys the large blocks that have 16 servings per block. If Rick has already eaten 5 servings of cheese, how many calories are remaining in the block?"""
    # Define the number of servings per block and calories per serving
    SERVINGS_PER_BLOCK = 16
    CALORIES_PER_SERVING = 110

    # Calculate the total number of calories per block
    total_calories = SERVINGS_PER_BLOCK * CALORIES_PER_SERVING

    # Calculate the number of calories consumed by Rick
    consumed_calories = 5 * CALORIES_PER_SERVING

    # Calculate the number of calories remaining
    remaining_calories = total_calories - consumed_calories

    result = remaining_calories
    return result

print(solution())