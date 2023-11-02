def solution():
    """Before getting to work, Jess has a few errands to run. Jess has to walk 11 blocks to the store and 6 blocks to the gallery, before walking the final 8 blocks to arrive at work. If Jess has already walked 5 blocks, how many more blocks must she walk before arriving at work?"""
    total_blocks = 11 + 6 + 8
    blocks_left = total_blocks - 5
    result = blocks_left
    return result

print(solution())