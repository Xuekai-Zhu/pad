def solution():
    """A box is 8 inches in height, 10 inches in width, and 12 inches in length. A wooden building block is 3 inches in height, 2 inches in width, and 4 inches in length. How many building blocks can fit into the box?"""
    # Define the dimensions of the box and the building block
    BOX_HEIGHT = 8
    BOX_WIDTH = 10
    BOX_LENGTH = 12
    BLOCK_HEIGHT = 3
    BLOCK_WIDTH = 2
    BLOCK_LENGTH = 4

    # Calculate the number of blocks that can fit in each dimension
    num_blocks_height = BOX_HEIGHT // BLOCK_HEIGHT
    num_blocks_width = BOX_WIDTH // BLOCK_WIDTH
    num_blocks_length = BOX_LENGTH // BLOCK_LENGTH

    # Calculate the total number of blocks that can fit in the box
    total_blocks = num_blocks_height * num_blocks_width * num_blocks_length

    # Display the total number of blocks that can fit in the box
    result = total_blocks
    return result

print(solution())