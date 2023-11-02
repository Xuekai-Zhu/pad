def solution():
    """Cooper is building a brick fence around all four sides of his property. Each of the four walls of his fence is 20 bricks long, 5 bricks high, and 2 bricks deep. How many bricks does Cooper need to complete his fence?"""
    # Define the dimensions of each brick
    BRICK_LENGTH = 1
    BRICK_WIDTH = 0.5
    BRICK_HEIGHT = 0.25

    # Define the dimensions of each wall
    WALL_LENGTH = 20
    WALL_HEIGHT = 5
    WALL_DEPTH = 2

    # Calculate the total number of bricks needed for one wall
    wall_bricks = WALL_LENGTH * WALL_HEIGHT * WALL_DEPTH * 2

    # Calculate the total number of bricks needed for all four walls
    total_bricks = wall_bricks * 4

    # Convert the total number of bricks to a whole number
    result = round(total_bricks / (BRICK_LENGTH * BRICK_WIDTH * BRICK_HEIGHT))

    return result

print(solution())