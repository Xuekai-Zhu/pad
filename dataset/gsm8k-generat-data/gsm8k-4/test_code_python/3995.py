def solution():
    """Kimiko is retiling her kitchen floor. Each tile is 6 square inches. If her kitchen is 48 inches by 72 inches, how many tiles does Kimiko need to buy?"""
    # Define the dimensions of the kitchen floor in inches
    width = 48
    length = 72

    # Calculate the total area of the kitchen floor in square inches
    area = width * length

    # Calculate the number of tiles needed, rounding up to the nearest whole number
    tiles_needed = math.ceil(area / 6)

    # Return the result
    result = tiles_needed
    return result

print(solution())