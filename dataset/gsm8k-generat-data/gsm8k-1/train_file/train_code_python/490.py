def solution():
    """Before getting to work, Jess has a few errands to run. Jess has to walk 11 blocks to the store and 6 blocks to the gallery, before walking the final 8 blocks to arrive at work. If Jess has already walked 5 blocks, how many more blocks must she walk before arriving at work?"""
    total_blocks = 11 + 6 + 8
    blocks_already_walked = 5
    blocks_left_to_walk = total_blocks - blocks_already_walked
    result = blocks_left_to_walk
    return result

print(solution())