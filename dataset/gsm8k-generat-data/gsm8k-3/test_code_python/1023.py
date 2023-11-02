def solution():
    """Cooper is building a brick fence around all four sides of his property.  Each of the four walls of his fence is 20 bricks long, 5 bricks high, and 2 bricks deep.  How many bricks does Cooper need to complete his fence?"""
    # Define the dimensions of each wall in bricks
    LENGTH = 20
    HEIGHT = 5
    DEPTH = 2

    # Calculate the number of bricks needed for each wall
    bricks_per_wall = LENGTH * HEIGHT * DEPTH

    # Calculate the total number of bricks needed for all four walls
    total_bricks = bricks_per_wall * 4

    # Display the total number of bricks needed
    result = total_bricks
    return result

print(solution())