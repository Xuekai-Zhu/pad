def solution():
    """Simeon drinks 64 fluid ounces of filtered water every day. He used to drink this water in 8-ounce-servings. But now, he drinks his water in 16-ounce servings. How many fewer servings per day does it now take Simeon to drink his water than it used to?"""
    # Define the amount of water Simeon drinks every day and the size of his old and new servings
    daily_water = 64
    old_serving_size = 8
    new_serving_size = 16

    # Calculate the number of servings Simeon used to need to drink his water
    old_num_servings = daily_water / old_serving_size

    # Calculate the number of servings Simeon now needs to drink his water
    new_num_servings = daily_water / new_serving_size

    # Calculate the difference in the number of servings
    num_servings_difference = old_num_servings - new_num_servings

    # Return the result
    result = num_servings_difference
    return result

print(solution())