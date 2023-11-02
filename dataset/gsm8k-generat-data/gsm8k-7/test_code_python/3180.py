def solution():
    calories_per_bread = 100
    calories_per_peanut_butter_serving = 200
    total_calories = 500

    # Calculate the remaining calories after one piece of bread
    remaining_calories = total_calories - calories_per_bread

    # Calculate the number of servings of peanut butter needed to reach the remaining calories
    num_peanut_butter_servings = remaining_calories / calories_per_peanut_butter_serving

    result = num_peanut_butter_servings
    return result

print(solution())