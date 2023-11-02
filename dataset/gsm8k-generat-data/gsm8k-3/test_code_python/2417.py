def solution():
    """Simeon drinks 64 fluid ounces of filtered water every day.  He used to drink this water in 8-ounce-servings.  But now, he drinks his water in 16-ounce servings.  How many fewer servings per day does it now take Simeon to drink his water than it used to?"""
    # Define the amount of water Simeon drinks in ounces and the size of his old and new servings
    water_oz = 64
    old_serving_size = 8
    new_serving_size = 16

    # Calculate the number of old servings and new servings
    old_servings = water_oz / old_serving_size
    new_servings = water_oz / new_serving_size

    # Calculate the difference in the number of servings
    difference = old_servings - new_servings

    # Display the difference in servings
    result = difference
    return result

print(solution())