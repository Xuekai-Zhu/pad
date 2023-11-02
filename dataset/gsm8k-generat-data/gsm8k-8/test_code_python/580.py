def solution():
    # Define the number of rows and number of bricks per row in the bottom half
    bottom_rows = 5
    bottom_bricks_per_row = 12

    # Define the number of rows and number of bricks per row in the top half
    top_rows = 5
    top_bricks_per_row = 8

    # Calculate the total number of bricks used in the bottom half and top half
    bottom_bricks = bottom_rows * bottom_bricks_per_row
    top_bricks = top_rows * top_bricks_per_row

    # Calculate the total number of bricks used in the entire igloo
    total_bricks = bottom_bricks + top_bricks
    result = total_bricks
    return result

print(solution())