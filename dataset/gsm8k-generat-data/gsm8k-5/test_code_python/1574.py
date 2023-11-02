def solution():
    bricks_per_row = 30  # Each row has 30 bricks
    rows_per_wall = 50  # Each wall has 50 rows

    # Calculate the total number of bricks used in both walls
    total_bricks = bricks_per_row * rows_per_wall * 2  # Two walls are being built

    result = total_bricks
    return result

print(solution())