def solution():
    
    camden_swims = 16
    susannah_swims = 24
    total_swims = camden_swims + susannah_swims
    swims_per_week = total_swims / 4
    camden_per_week = camden_swims / 4
    susannah_per_week = susannah_swims / 4
    difference = susannah_per_week - camden_per_week
    result = difference
    return result

print(solution())