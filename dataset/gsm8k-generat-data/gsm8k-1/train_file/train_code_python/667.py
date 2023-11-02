def solution():
    """A box is 8 inches in height, 10 inches in width, and 12 inches in length. A wooden building block is 3 inches in height, 2 inches in width, and 4 inches in length. How many building blocks can fit into the box?"""
    box_height = 8
    box_width = 10
    box_length = 12
    
    block_height = 3
    block_width = 2
    block_length = 4
    
    max_blocks_height = box_height // block_height
    max_blocks_width = box_width // block_width
    max_blocks_length = box_length // block_length
    
    total_blocks = max_blocks_height * max_blocks_width * max_blocks_length
    result = total_blocks
    
    return result

print(solution())