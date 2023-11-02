def solution():
    """Kimiko is retiling her kitchen floor. Each tile is 6 square inches. If her kitchen is 48 inches by 72 inches, how many tiles does Kimiko need to buy?"""
    # Calculate the area of Kimiko's kitchen
    kitchen_area = 48 * 72

    # Calculate the number of tiles needed to cover the kitchen floor
    num_tiles = kitchen_area / 6

    # Display the number of tiles needed
    result = num_tiles
    return result

print(solution())