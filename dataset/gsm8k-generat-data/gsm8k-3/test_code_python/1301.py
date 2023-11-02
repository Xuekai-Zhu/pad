def solution():
    """Each wall of a 3 sided shower has 8 tiles running the width of the wall and 20 tiles running the height of the wall.  How many tiles are in the shower?"""
    # Calculate the number of tiles on one wall
    wall_size = 8 * 20

    # Calculate the number of tiles on all three walls
    total_size = wall_size * 3

    # Display the total number of tiles
    result = total_size
    return result

print(solution())