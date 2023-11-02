def solution():
    # Define the number of bricks per row and number of rows per wall
    bricks_per_row = 30
    rows_per_wall = 50

    # Calculate the total number of bricks for both walls
    total_bricks = bricks_per_row * rows_per_wall * 2

    result = total_bricks
    return result

print(solution())