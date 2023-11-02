def solution():
    calories_per_serving = 110
    servings_per_block = 16
    servings_eaten = 5

    # Calculate the total number of servings remaining
    servings_remaining = servings_per_block - servings_eaten

    # Calculate the total number of calories remaining
    calories_remaining = servings_remaining * calories_per_serving
    result = calories_remaining
    return result

print(solution())