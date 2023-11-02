def solution():
    """Audrey's key lime pie calls for 1/4 cup of key lime juice but she likes to double this amount to make it extra tart. Each key lime yields 1 tablespoon of juice. There are 16 tablespoons in 1 cup. How many key limes does Audrey need?"""
    # Define the amount of juice needed in tablespoons
    juice_needed = 1/4 * 2 * 16

    # Calculate the number of key limes needed
    key_limes_needed = juice_needed / 1

    # Round up to the nearest whole number of limes
    key_limes_needed = round(key_limes_needed + 0.5)

    result = key_limes_needed
    return result

print(solution())