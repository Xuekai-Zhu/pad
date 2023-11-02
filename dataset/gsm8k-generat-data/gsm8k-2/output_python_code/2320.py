def solution():
    """Pete walked 5 blocks from his house to the bus garage in Houston. He rode the bus 20 blocks to the post office to get some stamps. Later, he came home the same way. How many blocks did Pete travel in all?"""
    blocks_to_garage = 5
    blocks_to_post_office = 20
    total_blocks = (blocks_to_garage * 2) + (blocks_to_post_office * 2)
    result = total_blocks
    return result

print(solution())