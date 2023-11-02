def solution():
    daily_water_intake = 64 # fluid ounces
    old_serving_size = 8 # fluid ounces
    new_serving_size = 16 # fluid ounces

    # Calculate the number of servings with the old serving size
    old_num_servings = daily_water_intake / old_serving_size

    # Calculate the number of servings with the new serving size
    new_num_servings = daily_water_intake / new_serving_size

    # Calculate the difference between the old and new number of servings
    fewer_servings_per_day = old_num_servings - new_num_servings
    result = fewer_servings_per_day
    return result

print(solution())