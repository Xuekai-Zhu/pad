def solution():
    """Toby is making toast and adding peanut butter to it. He wants to make sure he has 500 calories for breakfast. A piece of bread has 100 calories. A serving of peanut butter has 200 calories. If he has one piece of bread, how many servings of peanut butter should he add?"""
    # Define the calorie content of each item
    bread_calories = 100
    peanut_butter_calories = 200

    # Define the target number of calories for breakfast
    target_calories = 500

    # Calculate the number of servings of peanut butter needed to reach the target calories
    servings_needed = (target_calories - bread_calories) / peanut_butter_calories

    # Round up to the nearest whole serving
    servings_needed = round(servings_needed + 0.5)

    result = servings_needed
    return result

print(solution())