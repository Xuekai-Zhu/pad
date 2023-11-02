def solution():
    num_horses = 4
    oats_per_horse = 4
    grain_per_horse = 3
    meals_per_day = 3
    num_days = 3

    # Calculate the total amount of oats needed for all horses for all meals
    total_oats = num_horses * oats_per_horse * meals_per_day * num_days

    # Calculate the total amount of grain needed for all horses for all meals
    total_grain = num_horses * grain_per_horse * meals_per_day * num_days

    # Calculate the total amount of food needed for all horses for all meals
    total_food = total_oats + total_grain
    result = total_food
    return result

print(solution())