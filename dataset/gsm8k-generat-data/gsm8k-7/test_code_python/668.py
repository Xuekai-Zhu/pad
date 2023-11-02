def solution():
    box_height = 8
    box_width = 10
    box_length = 12

    block_height = 3
    block_width = 2
    block_length = 4

    # Calculate the number of blocks that can fit in each dimension
    num_blocks_height = box_height // block_height
    num_blocks_width = box_width // block_width
    num_blocks_length = box_length // block_length

    # Calculate the total number of blocks that can fit in the box
    total_blocks = num_blocks_height * num_blocks_width * num_blocks_length
    result = total_blocks
    return result

print(solution())