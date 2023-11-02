def solution():
    num_dogs = 4
    servings_per_day = 2
    grams_per_serving = 250 / 1000  # Convert to kilograms
    num_sacks = 2
    sack_weight = 50  # kilograms per sack

    # Calculate the total amount of food needed per day for all dogs
    total_food_per_day = num_dogs * servings_per_day * grams_per_serving

    # Calculate how many days the food will last
    total_food = num_sacks * sack_weight
    days_of_food = total_food / total_food_per_day
    result = days_of_food
    return result

print(solution())