def solution():
    # Calculate the volume of the box
    box_volume = 8 * 10 * 12

    # Calculate the volume of a wooden block
    block_volume = 3 * 2 * 4

    # Calculate the number of blocks that can fit into the box
    num_blocks = box_volume // block_volume

    result = num_blocks
    return result

print(solution())