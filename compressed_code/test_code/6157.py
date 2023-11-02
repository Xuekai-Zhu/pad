def solution():
    
    total_blocks = 11 + 6 + 8
    blocks_already_walked = 5
    blocks_left_to_walk = total_blocks - blocks_already_walked
    result = blocks_left_to_walk
    return result

print(solution())