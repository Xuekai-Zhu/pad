def solution():
    calories_per_serving = 110
    servings_per_block = 16
    servings_eaten = 5
    calories_per_block = calories_per_serving * servings_per_block
    calories_remaining = calories_per_block - (calories_per_serving * servings_eaten)
    result = calories_remaining
    return result

print(solution())