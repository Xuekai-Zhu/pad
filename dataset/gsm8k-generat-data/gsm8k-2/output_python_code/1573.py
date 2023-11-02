def solution():
    """Two brick walls are being built. Each wall has 30 bricks in a single row and there are 50 rows in each wall. How many bricks will be used to make both walls?"""
    brick_rows = 50
    bricks_per_row = 30
    total_bricks = 2 * brick_rows * bricks_per_row
    result = total_bricks
    return result

print(solution())