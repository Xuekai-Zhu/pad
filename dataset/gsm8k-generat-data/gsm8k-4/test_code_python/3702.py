def solution():
    """Janet is considering two options to retile her bathroom. The turquoise tiles cost $13/tile and the purple tiles cost $11/tile. If Janet needs to tile two walls that measure 5 feet by 8 feet and 7 feet by 8 feet, and each square foot of wall takes 4 tiles, how much will Janet save by buying the purple tiles instead of the turquoise ones?"""
    # Define the dimensions of each wall in feet
    wall1_length = 5
    wall1_width = 8
    wall2_length = 7
    wall2_width = 8

    # Define the number of tiles needed to tile each wall
    wall1_tiles = wall1_length * wall1_width * 4
    wall2_tiles = wall2_length * wall2_width * 4

    # Define the prices of each tile
    turquoise_price = 13
    purple_price = 11

    # Calculate the total cost of tiling with turquoise tiles
    turquoise_cost = wall1_tiles * turquoise_price + wall2_tiles * turquoise_price

    # Calculate the total cost of tiling with purple tiles
    purple_cost = wall1_tiles * purple_price + wall2_tiles * purple_price

    # Calculate the amount saved by buying purple tiles instead of turquoise tiles
    amount_saved = turquoise_cost - purple_cost

    # Return the result
    result = amount_saved
    return result

print(solution())