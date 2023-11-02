def solution():
    """Two brick walls are being built. Each wall has 30 bricks in a single row and there are 50 rows in each wall. How many bricks will be used to make both walls?"""
    bricks_per_row = 30
    rows_per_wall = 50
    total_bricks = bricks_per_row * rows_per_wall * 2
    result = total_bricks
    return result

print(solution())