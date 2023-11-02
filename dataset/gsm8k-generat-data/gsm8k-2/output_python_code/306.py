def solution():
    """There are 110 calories in a serving of cheese. Rick buys the large blocks that have 16 servings per block. If Rick has already eaten 5 servings of cheese, how many calories are remaining in the block?"""
    servings_per_block = 16
    calories_per_serving = 110
    servings_remaining = servings_per_block - 5
    calories_remaining = servings_remaining * calories_per_serving
    result = calories_remaining
    return result

print(solution())