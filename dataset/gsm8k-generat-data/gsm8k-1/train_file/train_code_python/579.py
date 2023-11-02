def solution():
    """Libby is building an igloo in her backyard using bricks of snow. She builds her igloo in rows, using a total of 10 rows of bricks of snow. The bottom half of the igloo has 12 bricks of snow in each row while the top half of the igloo has 8 bricks of snow in each row. How many bricks of snow did Libby use for her igloo?"""
    bottom_half_rows = 5
    top_half_rows = 5
    bottom_half_bricks = 12
    top_half_bricks = 8
    total_bricks = (bottom_half_rows * bottom_half_bricks) + (top_half_rows * top_half_bricks)
    result = total_bricks
    return result

print(solution())