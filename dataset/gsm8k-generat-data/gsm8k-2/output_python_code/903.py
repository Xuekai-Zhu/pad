def solution():
    """Audrey's key lime pie calls for 1/4 cup of key lime juice but she likes to double this amount to make it extra tart. Each key lime yields 1 tablespoon of juice. There are 16 tablespoons in 1 cup. How many key limes does Audrey need?"""
    juice_needed = 1 / 4 * 2  # Double the amount for extra tartness
    tablespoons_needed = juice_needed * 16  # Convert to tablespoons
    key_limes_needed = tablespoons_needed / 1  # Each key lime yields 1 tablespoon of juice
    result = key_limes_needed
    return result

print(solution())