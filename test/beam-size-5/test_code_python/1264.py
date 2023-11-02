def solution():
    
    blue_blocks = 4
    yellow_blocks = blue_blocks * 2
    total_blocks = 32
    red_blocks = total_blocks - blue_blocks - yellow_blocks
    result = red_blocks
    return result

print(solution())