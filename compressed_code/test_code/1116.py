def solution():
    
    ties = 34
    belts = 40
    black_shirts = 63
    white_shirts = 42
    jeans = (2/3 * (black_shirts + white_shirts))
    scarves = 1/2 * (ties + belts)
    difference = jeans - scarves
    result = difference
    return result

print(solution())