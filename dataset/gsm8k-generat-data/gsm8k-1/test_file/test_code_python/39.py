def solution():
    """According to its nutritional info, a bag of chips has 250 calories per serving. If a 300g bag has 5 servings, how many grams can you eat if your daily calorie target is 2000 and you have already consumed 1800 calories?"""
    bag_weight = 300
    servings_per_bag = 5
    calorie_per_serving = 250
    max_calories = 2000
    consumed_calories = 1800
    
    # Calculate the total calories in the bag
    total_calories = servings_per_bag * calorie_per_serving
    
    # Calculate the remaining calories the person can consume
    remaining_calories = max_calories - consumed_calories
    
    # Calculate the maximum grams of chips the person can eat
    max_grams = (remaining_calories / calorie_per_serving) * bag_weight
    
    # Round the result to two decimal places
    result = round(max_grams, 2)
    
    return result

print(solution())