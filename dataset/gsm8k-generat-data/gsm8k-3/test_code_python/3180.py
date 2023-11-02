def solution():
    """Toby is making toast and adding peanut butter to it. He wants to make sure he has 500 calories for breakfast. A piece of bread has 100 calories. A serving of peanut butter has 200 calories. If he has one piece of bread, how many servings of peanut butter should he add?"""
    # Define the number of calories in a piece of bread and a serving of peanut butter
    BREAD_CALORIES = 100
    PEANUT_BUTTER_CALORIES = 200

    # Define the total number of calories Toby wants for breakfast
    TOTAL_CALORIES = 500

    # Calculate the number of servings of peanut butter Toby should add
    bread_calories = BREAD_CALORIES
    peanut_butter_calories = TOTAL_CALORIES - bread_calories
    servings_of_peanut_butter = peanut_butter_calories / PEANUT_BUTTER_CALORIES

    # Display the number of servings of peanut butter Toby should add
    result = servings_of_peanut_butter
    return result

print(solution())