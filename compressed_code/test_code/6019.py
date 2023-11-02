def solution():
    
    calories_per_serving = 110
    servings_per_block = 16
    servings_eaten = 5
    servings_remaining = servings_per_block - servings_eaten
    total_calories = servings_remaining * calories_per_serving
    result = total_calories
    return result

print(solution())