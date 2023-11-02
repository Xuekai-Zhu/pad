def solution():
    # Calculate the volume of the box and the volume of one building block
    box_volume = 8 * 10 * 12
    block_volume = 3 * 2 * 4

    # Calculate how many blocks can fit into the box
    blocks_in_box = box_volume // block_volume  # Use integer division to get a whole number

    result = blocks_in_box
    return result

print(solution())