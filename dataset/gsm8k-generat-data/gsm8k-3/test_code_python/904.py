def solution():
    """Audrey's key lime pie calls for 1/4 cup of key lime juice but she likes to double this amount to make it extra tart.  Each key lime yields 1 tablespoon of juice.  There are 16 tablespoons in 1 cup.  How many key limes does Audrey need?"""
    # Define the amount of key lime juice needed
    JUICE_NEEDED = 0.25 # in cups

    # Double the amount of key lime juice needed
    JUICE_NEEDED *= 2

    # Convert the amount of key lime juice needed to tablespoons
    JUICE_NEEDED *= 16

    # Calculate the number of key limes needed
    LIMES_NEEDED = JUICE_NEEDED / 1 # 1 key lime yields 1 tablespoon of juice

    # Round up to the nearest whole number of key limes
    LIMES_NEEDED = int(math.ceil(LIMES_NEEDED))

    # Display the number of key limes needed
    result = LIMES_NEEDED
    return result

print(solution())