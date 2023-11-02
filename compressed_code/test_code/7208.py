def solution():
    
    preprinted = 16
    remaining = 36 - preprinted
    hand_written = remaining / 2
    not_wearing = 36 - preprinted - hand_written
    result = not_wearing
    return result

print(solution())