def solution():
    # Define calorie values
    bread_calories = 100
    peanut_butter_calories = 200

    # Calculate how many servings of peanut butter are needed
    servings_of_peanut_butter = (500 - bread_calories) / peanut_butter_calories

    result = servings_of_peanut_butter
    return result

print(solution())