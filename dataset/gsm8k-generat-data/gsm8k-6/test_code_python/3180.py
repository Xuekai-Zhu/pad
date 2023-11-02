def solution():
    # Calculate the number of servings of peanut butter Toby should add to reach the total calorie requirement of 500
    calories_from_bread = 100  # calories in one piece of bread
    calories_from_peanut_butter = 200  # calories in one serving of peanut butter
    total_calories_required = 500
    servings_of_peanut_butter = (total_calories_required - calories_from_bread) / calories_from_peanut_butter
    result = servings_of_peanut_butter
    return result

print(solution())