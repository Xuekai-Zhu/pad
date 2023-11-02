def solution():
    daily_water_consumption = 64  # Simeon drinks 64 fluid ounces of water every day
    old_serving_size = 8  # Simeon used to drink his water in 8-ounce servings
    new_serving_size = 16  # Simeon now drinks his water in 16-ounce servings

    # Calculate the number of servings Simeon used to drink with the old serving size
    old_num_servings = daily_water_consumption / old_serving_size

    # Calculate the number of servings Simeon now drinks with the new serving size
    new_num_servings = daily_water_consumption / new_serving_size

    # Calculate the difference in the number of servings consumed each day
    diff_num_servings = old_num_servings - new_num_servings
    result = diff_num_servings
    return result

print(solution())