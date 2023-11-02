def solution():
    """Tara has a shoebox that is 4 inches tall and 6 inches wide. She puts a square block inside that is 4 inches per side. How many square inches of the box are left uncovered?"""
    # Define the dimensions of the shoebox and the block
    box_height = 4
    box_width = 6
    block_side = 4

    # Calculate the area of the shoebox
    box_area = box_height * box_width

    # Calculate the area of the block
    block_area = block_side * block_side

    # Calculate the area of the uncovered space
    uncovered_area = box_area - block_area

    # return the result
    result = uncovered_area
    return result

print(solution())