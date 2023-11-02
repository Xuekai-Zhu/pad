def solution():
    num_bricks_in_row = 30
    num_rows = 50

    # Calculate the total number of bricks needed for one wall
    total_bricks_one_wall = num_bricks_in_row * num_rows

    # Calculate the total number of bricks needed for both walls
    total_bricks_both_walls = total_bricks_one_wall * 2
    result = total_bricks_both_walls
    return result

print(solution())