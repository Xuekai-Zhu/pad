def solution():
    
    servings_per_block = 16
    calories_per_serving = 110
    servings_remaining = servings_per_block - 5
    calories_remaining = servings_remaining * calories_per_serving
    result = calories_remaining
    return result

print(solution())