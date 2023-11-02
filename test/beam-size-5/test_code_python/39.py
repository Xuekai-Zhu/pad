def solution():
    calories_per_serving = 250  # Each bag of chips has 250 calories
    servings_per_bag = 5  # A 300g bag has 5 servings
    target_daily_calories = 2000  # Your daily calorie target is 2000 days
    calories_consumed = 1800  # Your daily calorie target is 1800 calories

    # Calculate the total calories consumed in the bag
    total_calories_consumed = servings_per_bag * calories_per_serving * servings_per_bag

    # Calculate the total calories consumed in grams
    total_calories_in_grams = total_calories_consumed / calories_per_serving
    result = total_calories_in_grams
    return result

print(solution())