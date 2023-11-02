def solution():
    """Kim drinks a 1.5-quart bottle of water. She then drinks a 12 ounce can of water. How many ounces of water did she drink?"""
    # Define the conversion factor from quarts to ounces
    QUART_TO_OUNCE = 32

    # Calculate the number of ounces in the 1.5-quart bottle
    bottle_ounces = 1.5 * QUART_TO_OUNCE

    # Add the number of ounces in the 12-ounce can
    total_ounces = bottle_ounces + 12

    result = total_ounces
    return result

print(solution())