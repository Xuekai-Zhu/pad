def solution():
    num_dogs = 4
    daily_food_per_dog = 250  # in grams
    num_days = 14

    # Calculate the total food needed in grams
    total_food_in_grams = num_dogs * daily_food_per_dog * num_days

    # Convert the total food to kilograms
    total_food_in_kg = total_food_in_grams / 1000
    result = total_food_in_kg
    return result

print(solution())