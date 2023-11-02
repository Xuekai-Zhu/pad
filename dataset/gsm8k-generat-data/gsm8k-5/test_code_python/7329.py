def solution():
    box_height = 4  # The height of the shoebox is 4 inches
    box_width = 6  # The width of the shoebox is 6 inches
    block_side = 4  # The side of the square block is 4 inches

    # Calculate the area occupied by the block
    block_area = block_side ** 2

    # Calculate the area of the base of the shoebox
    box_base_area = box_height * box_width

    # Calculate the area left uncovered
    uncovered_area = box_base_area - block_area
    result = uncovered_area
    return result

print(solution())