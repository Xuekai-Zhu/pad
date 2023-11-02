def solution():
    """There are 110 calories in a serving of cheese. Rick buys the large blocks that have 16 servings per block. If Rick has already eaten 5 servings of cheese, how many calories are remaining in the block?"""
    calories_per_serving = 110
    servings_per_block = 16
    servings_eaten = 5
    servings_remaining = servings_per_block - servings_eaten
    total_calories = servings_remaining * calories_per_serving
    result = total_calories
    return result

print(solution())