def solution():
    """A box is 8 inches in height, 10 inches in width, and 12 inches in length. A wooden building block is 3 inches in height, 2 inches in width, and 4 inches in length. How many building blocks can fit into the box?"""
    # Define the dimensions of the box and the building block
    box_height = 8
    box_width = 10
    box_length = 12
    block_height = 3
    block_width = 2
    block_length = 4

    # Calculate the number of blocks that can fit along each dimension of the box
    num_blocks_height = box_height // block_height
    num_blocks_width = box_width // block_width
    num_blocks_length = box_length // block_length

    # Calculate the total number of blocks that can fit in the box
    num_blocks = num_blocks_height * num_blocks_width * num_blocks_length

    # Return the result
    result = num_blocks
    return result

print(solution())