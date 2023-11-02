def solution():
    
    
    ties = 34
    belts = 40
    black_shirts = 63
    white_shirts = 42
    
    jeans = (black_shirts + white_shirts) * (2/3)
    scarves = (ties + belts) * 0.5
    
    difference = jeans - scarves
    
    result = difference
    
    return result

print(solution())