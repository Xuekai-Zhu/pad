def solution():
    """Libby is building an igloo in her backyard using bricks of snow. She builds her igloo in rows, using a total of 10 rows of bricks of snow. The bottom half of the igloo has 12 bricks of snow in each row while the top half of the igloo has 8 bricks of snow in each row. How many bricks of snow did Libby use for her igloo?"""
    # Define the number of rows in the bottom half and top half of the igloo
    bottom_rows = 5
    top_rows = 5

    # Define the number of bricks in each row for the bottom and top half of the igloo
    bottom_bricks = 12
    top_bricks = 8

    # Calculate the total number of bricks of snow used in the bottom half of the igloo
    bottom_total = bottom_rows * bottom_bricks

    # Calculate the total number of bricks of snow used in the top half of the igloo
    top_total = top_rows * top_bricks

    # Calculate the total number of bricks of snow used for the whole igloo
    total = bottom_total + top_total

    # return the result
    result = total
    return result

print(solution())