def solution():
    # Calculate the number of key limes needed for Audrey's pie
    juice_needed = 1/4 * 2  # double the amount of key lime juice called for in the recipe
    tablespoons_needed = juice_needed * 16  # convert from cups to tablespoons
    key_limes_needed = tablespoons_needed * (1/2)  # each key lime yields 1 tablespoon of juice
    result = key_limes_needed
    return result

print(solution())