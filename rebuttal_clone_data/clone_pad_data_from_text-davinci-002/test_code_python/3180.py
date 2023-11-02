def solution():
    calories_needed = 500
    calories_per_bread = 100
    calories_per_peanut_butter = 200
    servings_of_peanut_butter = (calories_needed - calories_per_bread) / calories_per_peanut_butter
    result = servings_of_peanut_butter
    return result

print(solution())