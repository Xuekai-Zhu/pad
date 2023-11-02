def solution():
    pieces_per_block = 30
    blocks_used = 3
    candies_used = pieces_per_block * blocks_used
    necklaces_made = candies_used / 10
    result = necklaces_made
    return result

print(solution())