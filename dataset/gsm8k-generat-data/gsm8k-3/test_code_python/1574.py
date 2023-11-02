def solution():
    """Two brick walls are being built. Each wall has 30 bricks in a single row and there are 50 rows in each wall. How many bricks will be used to make both walls?"""
    # Define the number of bricks in a single row and the number of rows in each wall
    BRICKS_PER_ROW = 30
    ROWS_PER_WALL = 50

    # Calculate the total number of bricks in both walls
    total_bricks = 2 * BRICKS_PER_ROW * ROWS_PER_WALL

    # Display the total number of bricks
    result = total_bricks
    return result

print(solution())