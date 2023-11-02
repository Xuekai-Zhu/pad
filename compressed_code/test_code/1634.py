def solution():
    
    sandbox_side = 40
    sandbox_area = sandbox_side ** 2
    sandbag_area = 80
    sandbag_weight = 30
    sand_needed = (sandbox_area / sandbag_area) * sandbag_weight
    result = sand_needed
    return result

print(solution())