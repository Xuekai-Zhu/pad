def solution():
    box_height = 4
    box_width = 6
    block_side = 4

    # Calculate the area of the shoebox
    box_area = box_height * box_width

    # Calculate the area of the block
    block_area = block_side ** 2

    # Calculate the area of the uncovered space
    uncovered_area = box_area - block_area
    result = uncovered_area
    return result

print(solution())