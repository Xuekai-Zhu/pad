def solution():
    """Janet is considering two options to retile her bathroom. The turquoise tiles cost $13/tile and the purple tiles cost $11/tile. If Janet needs to tile two walls that measure 5 feet by 8 feet and 7 feet by 8 feet, and each square foot of wall takes 4 tiles, how much will Janet save by buying the purple tiles instead of the turquoise ones?"""
    
    # Calculate the total area of the walls to be tiled in square feet
    total_area = (5*8*2) + (7*8*2) # 2 walls to be tiled

    # Calculate the total number of tiles needed for each type
    turquoise_tiles = total_area * 4
    purple_tiles = turquoise_tiles

    # Calculate the cost of each type of tile
    turquoise_cost = turquoise_tiles * 13
    purple_cost = purple_tiles * 11

    # Calculate the amount saved by buying the purple tiles
    savings = turquoise_cost - purple_cost

    # Display the amount saved
    result = savings
    return result

print(solution())