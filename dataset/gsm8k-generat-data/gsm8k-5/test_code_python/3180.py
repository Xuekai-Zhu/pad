def solution():
    bread_calories = 100  # A piece of bread has 100 calories
    pb_calories = 200  # A serving of peanut butter has 200 calories
    total_calories = 500  # Toby wants 500 calories for breakfast

    # Calculate the number of servings of peanut butter needed to reach 500 calories
    servings_pb = (total_calories - bread_calories) / pb_calories
    result = servings_pb
    return result

print(solution())