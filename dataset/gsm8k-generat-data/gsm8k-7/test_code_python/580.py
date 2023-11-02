def solution():
    total_rows = 10
    bottom_half_rows = 5
    top_half_rows = 5
    bottom_half_bricks = 12
    top_half_bricks = 8

    # Calculate the total number of bricks in the bottom half of the igloo
    total_bottom_half_bricks = bottom_half_rows * bottom_half_bricks

    # Calculate the total number of bricks in the top half of the igloo
    total_top_half_bricks = top_half_rows * top_half_bricks

    # Calculate the total number of bricks used for the entire igloo
    total_bricks = total_bottom_half_bricks + total_top_half_bricks
    result = total_bricks
    return result

print(solution())