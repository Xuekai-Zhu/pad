def solution():
    
    servings_per_package = 3
    calories_per_serving = 120
    servings_eaten = servings_per_package / 2
    calories_eaten = servings_eaten * calories_per_serving
    result = calories_eaten
    return result

print(solution())