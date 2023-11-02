def solution():
    # Calculate the total number of bricks required for one wall
    bricks_per_wall = 20 * 5 * 2  # 20 bricks long, 5 bricks high, and 2 bricks deep

    # Calculate the total number of bricks required for all four walls
    total_bricks = bricks_per_wall * 4

    result = total_bricks
    return result

print(solution())