def solution():
    box_volume = 8 * 10 * 12  # Volume of the box is 8x10x12 = 960 cubic inches
    block_volume = 3 * 2 * 4  # Volume of one block is 3x2x4 = 24 cubic inches

    # Calculate the number of building blocks that can fit in the box
    num_blocks = box_volume // block_volume
    result = num_blocks
    return result

print(solution())