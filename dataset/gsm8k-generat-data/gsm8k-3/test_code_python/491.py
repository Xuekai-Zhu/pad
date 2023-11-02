def solution():
    """Before getting to work, Jess has a few errands to run. Jess has to walk 11 blocks to the store and 6 blocks to the gallery, before walking the final 8 blocks to arrive at work. If Jess has already walked 5 blocks, how many more blocks must she walk before arriving at work?"""
    
    # Calculate the total number of blocks Jess has to walk
    total_blocks = 11 + 6 + 8

    # Calculate the number of blocks Jess has already walked
    walked_blocks = 5

    # Calculate the number of blocks Jess has left to walk
    left_blocks = total_blocks - walked_blocks

    # Display the number of blocks Jess has left to walk
    result = left_blocks
    return result

print(solution())