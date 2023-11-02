def solution():
    """Two brick walls are being built. Each wall has 30 bricks in a single row and there are 50 rows in each wall. How many bricks will be used to make both walls?"""
    # Define the number of bricks per row and the number of rows per wall
    BRICKS_PER_ROW = 30
    ROWS_PER_WALL = 50

    # Calculate the total number of bricks for one wall
    bricks_per_wall = BRICKS_PER_ROW * ROWS_PER_WALL

    # Calculate the total number of bricks for both walls
    bricks_total = bricks_per_wall * 2

    # Return the result
    result = bricks_total
    return result

print(solution())