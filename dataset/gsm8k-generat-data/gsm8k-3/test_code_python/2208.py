def solution():
    """Steve is building a bench for the playground and needs 6 lengths of wood that measure 4 feet and 2 lengths of wood that measure 2 feet. How many feet of wood does Steve need to buy?"""
    # Define the length of wood needed for each piece
    LONG_WOOD_LENGTH = 4
    SHORT_WOOD_LENGTH = 2

    # Define the number of each type of wood needed
    long_wood_count = 6
    short_wood_count = 2

    # Calculate the total length of the long wood needed
    long_wood_length = long_wood_count * LONG_WOOD_LENGTH

    # Calculate the total length of the short wood needed
    short_wood_length = short_wood_count * SHORT_WOOD_LENGTH

    # Calculate the total length of wood needed
    total_length = long_wood_length + short_wood_length

    # Display the total length needed
    result = total_length
    return result

print(solution())