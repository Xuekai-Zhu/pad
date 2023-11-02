def solution():
    total_rows = 10  # Libby uses a total of 10 rows of bricks
    bottom_rows = total_rows // 2  # The bottom half of the igloo has half of the total rows
    top_rows = total_rows - bottom_rows  # The top half of the igloo has the remaining rows
    bottom_bricks_per_row = 12  # The bottom half of the igloo has 12 bricks per row
    top_bricks_per_row = 8  # The top half of the igloo has 8 bricks per row

    # Calculate the total number of bricks used in the bottom half of the igloo
    bottom_bricks = bottom_rows * bottom_bricks_per_row

    # Calculate the total number of bricks used in the top half of the igloo
    top_bricks = top_rows * top_bricks_per_row

    # Calculate the total number of bricks used in the entire igloo
    total_bricks = bottom_bricks + top_bricks
    result = total_bricks
    return result

print(solution())