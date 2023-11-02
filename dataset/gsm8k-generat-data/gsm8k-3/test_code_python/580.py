def solution():
    """Libby is building an igloo in her backyard using bricks of snow. She builds her igloo in rows, using a total of 10 rows of bricks of snow. The bottom half of the igloo has 12 bricks of snow in each row while the top half of the igloo has 8 bricks of snow in each row. How many bricks of snow did Libby use for her igloo?"""
    # Define the number of rows and bricks per row
    ROWS = 10
    BOTTOM_ROW_BRICKS = 12
    TOP_ROW_BRICKS = 8

    # Calculate the number of bricks in the bottom half of the igloo
    bottom_half_bricks = (ROWS // 2) * BOTTOM_ROW_BRICKS

    # Calculate the number of bricks in the top half of the igloo
    top_half_bricks = (ROWS // 2) * TOP_ROW_BRICKS

    # Calculate the total number of bricks used
    total_bricks = bottom_half_bricks + top_half_bricks

    # Display the total number of bricks used
    result = total_bricks
    return result

print(solution())