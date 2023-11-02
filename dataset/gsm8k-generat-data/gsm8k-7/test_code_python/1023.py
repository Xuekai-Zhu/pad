def solution():
    brick_length = 20
    brick_height = 5
    brick_depth = 2

    # Calculate the number of bricks needed for one wall
    bricks_per_wall = brick_length * brick_height * brick_depth

    # Calculate the total number of bricks needed for all four walls
    total_bricks = bricks_per_wall * 4
    result = total_bricks
    return result

print(solution())