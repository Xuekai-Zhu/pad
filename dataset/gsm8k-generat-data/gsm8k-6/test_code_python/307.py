def solution():
    # Calculate the total number of calories in a block of cheese
    calories_in_block = 110 * 16  # 110 calories per serving, 16 servings per block

    # Calculate the number of calories Rick has already consumed
    calories_consumed = 110 * 5  # 110 calories per serving, 5 servings eaten

    # Calculate the remaining number of calories in the block of cheese
    calories_remaining = calories_in_block - calories_consumed

    result = calories_remaining
    return result

print(solution())