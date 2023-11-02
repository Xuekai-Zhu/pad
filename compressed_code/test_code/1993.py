def solution():
    
    agate_precious_stones = 30
    olivine_precious_stones = agate_precious_stones + 5
    diamond_precious_stones = olivine_precious_stones + 11
    total_precious_stones = agate_precious_stones + olivine_precious_stones + diamond_precious_stones
    result = total_precious_stones
    return result

print(solution())