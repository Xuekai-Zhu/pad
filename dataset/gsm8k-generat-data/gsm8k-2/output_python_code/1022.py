def solution():
    """Cooper is building a brick fence around all four sides of his property.
    Each of the four walls of his fence is 20 bricks long, 5 bricks high, and 2 bricks deep.
    How many bricks does Cooper need to complete his fence?"""

    # Calculate the number of bricks needed for one wall
    wall_length = 20
    wall_height = 5
    wall_depth = 2
    wall_bricks = wall_length * wall_height * wall_depth

    # Calculate the number of bricks needed for all four walls
    total_wall_bricks = wall_bricks * 4

    result = total_wall_bricks
    return result

print(solution())